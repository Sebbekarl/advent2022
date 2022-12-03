
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;





fn main() {
    let mut sum = 0;

    if let Ok(lines) = read_lines("input.txt") {
        for line in lines {
            if let Ok(ip) = line {
                sum = handle_input_line(ip, sum);

            }
        }
    }
    println!("{}",sum)
}


fn handle_input_line(ip: String, mut sum: u32) -> u32{
    let input_str = ip.bytes().map(Into::<u32>::into).collect::<Vec<_>>();
    
    let mut foundChars: Vec<u32> = Vec::new();
    
    for i in 0..input_str.len()/2 {
        for j in 0..input_str.len()/2{

            if input_str[i] == input_str[input_str.len()-1-j] {
                if !foundChars.contains(&input_str[i]) {

                    foundChars.push(input_str[i]);
                    println!("{}", ascii_to_prio(input_str[i]));
                    sum += ascii_to_prio(input_str[i]);
                    
                }
                break;
            }

        }

    }

    return sum;

}


fn ascii_to_prio(ascii_num: u32) -> u32 {
    if ascii_num > 96 {
        return ascii_num - 96;
    }else{
        return ascii_num-64+26;
    }
}


fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
