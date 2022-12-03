use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut sum = 0;
    let mut input_strings: Vec<String> = vec![];
    
    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            if let Ok(ip) = line {
                input_strings.push(ip);
            }
        }
    }

    for i in (0..input_strings.len()).step_by(3){
        sum = handle_input_lines(&input_strings[i], &input_strings[i+1], &input_strings[i+2], sum);
    }

    println!("{}",sum)
}

fn handle_input_lines(ip1: &String,ip2: &String, ip3: &String, mut sum: u32) -> u32 {

    let temp1 = ip1.bytes().map(Into::<u32>::into).collect::<Vec<_>>();
    let temp2 = ip2.bytes().map(Into::<u32>::into).collect::<Vec<_>>();
    let temp3 = ip3.bytes().map(Into::<u32>::into).collect::<Vec<_>>();

    for i in 0..temp1.len() {
        if temp2.contains(&temp1[i]) {
            if temp3.contains(&temp1[i]){
                sum += ascii_to_prio(temp1[i]);
                break;
            }
        }    
    }
    
    return sum;
}

fn ascii_to_prio(ascii_num: u32) -> u32 {
    if ascii_num > 96 {
        return ascii_num - 96;
    } else {
        return ascii_num - 64 + 26;
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
