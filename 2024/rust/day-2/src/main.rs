use std::fs;

mod day_2_1;
mod day_2_2;

fn main() {
    const _TEST_DATA: &str = "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9";

    const FILE_PATH: &str = "input.txt";
    let contents = fs::read_to_string(FILE_PATH).expect("Should have been able to read the file");

    // day_2_1::run(_TEST_DATA);
    // day_2_1::run(&contents);

    // day_2_2::run(_TEST_DATA);
    day_2_2::run(&contents);
}
