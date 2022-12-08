use std::collections::HashMap;

type Filesystem = HashMap<String, usize>;

fn main() {
    let input = include_str!("input.txt").trim();
    let filesystem = get_filesystem(input);

    let part_1: usize = filesystem.values().filter(|&sum| *sum <= 100_000).sum();
    let part_2 = *filesystem.values().min_by_key(|f| f.abs_diff((filesystem["/"] - 40_000_000) as usize)).unwrap();

    println!("{}", part_1);
    println!("{}", part_2);
}

fn get_filesystem(input: &str) -> Filesystem {
    let mut cur_dir = Vec::new();
    let mut dirs = HashMap::new();

    input
        .split("$ ")
        .skip(1)
        .map(|part| {
            let (ins, data) = part.split_at(2);
            (ins, data.trim())
        })
        .for_each(|instruction| {
            match instruction {
                ("cd", "/") => {
                    cur_dir.clear();
                    cur_dir.push(String::from("/"));
                }
                ("cd", "..") => {
                    cur_dir.pop();
                }
                ("cd", dirname) => {
                    let last_dir = cur_dir.last().unwrap();
                    cur_dir.push(format!("{last_dir}, {dirname}/"));
                }
                ("ls", data) => {
                    println!("{}", data);
                    data.lines()
                        .map(|l| l.split_whitespace().next().unwrap())
                        .filter_map(|filesize| filesize.parse::<usize>().ok())
                        .for_each(|filesize| {
                            cur_dir.iter().cloned().for_each(|dir| {
                                dirs
                                    .entry(dir)
                                    .and_modify(|size| *size += filesize)
                                    .or_insert(filesize);
                            })
                        });
                }
                _ => panic!("error in matching"),
            };
        });

    dirs
}

