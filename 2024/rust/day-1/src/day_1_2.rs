use std::collections::HashMap;

pub fn run(data: &str) {
    let lines = data.split('\n');
    let mut left_col = Vec::new();
    let mut right_col = HashMap::new();

    for line in lines {
        let t = line.split_once("   ").unwrap();
        let left: u32 = t.0.parse().unwrap();
        let right: u32 = t.1.parse().unwrap();
        left_col.push(left);
        *right_col.entry(right).or_insert(0) += 1_u32;
    }

    let mut sum_of_mul: u32 = 0;
    for val in left_col {
        // diffs += left_col[i].abs_diff(right_col[i])
        sum_of_mul += val * right_col.get(&val).unwrap_or(&0);
    }

    println!("{}", sum_of_mul)
}
