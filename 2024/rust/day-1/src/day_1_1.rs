pub fn run(data: &str) {
    let lines = data.split('\n');
    let mut left_col = Vec::new();
    let mut right_col = Vec::new();
    for line in lines {
        let t = line.split_once("   ").unwrap();
        let left: u32 = t.0.parse().unwrap();
        let right: u32 = t.1.parse().unwrap();
        left_col.push(left);
        right_col.push(right);
    }

    left_col.sort();
    right_col.sort();

    let mut diffs: u32 = 0;
    for i in 0..left_col.len() {
        diffs += left_col[i].abs_diff(right_col[i])
    }

    println!("{}", diffs)
}
