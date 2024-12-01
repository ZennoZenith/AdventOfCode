use std::fs;

mod day_1_1;
mod day_1_2;

fn main() {
    const _TEST_DATA: &str = "3   4
4   3
2   5
1   3
3   9
3   3";

    const FILE_PATH: &str = "input.txt";
    let contents = fs::read_to_string(FILE_PATH).expect("Should have been able to read the file");

    // day_1_1::run(_TEST_DATA);
    // day_1_1::run(&contents);

    // day_1_2::run(_TEST_DATA);
    day_1_2::run(&contents);
}
