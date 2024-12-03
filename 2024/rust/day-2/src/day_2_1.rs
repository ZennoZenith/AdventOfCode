fn check_diff_vec(diff_vec: &[i32]) -> i32 {
    let mut invalid_index = -1;
    // Check for ascending
    diff_vec.iter().enumerate().for_each(|(i, val)| {
        if !(1..=3).contains(val) {
            invalid_index = i as i32;
        }
    });

    if invalid_index == -1 {
        return invalid_index;
    }

    invalid_index = -1;
    // Check for descending
    diff_vec.iter().enumerate().for_each(|(i, val)| {
        if !(1..=3).contains(&-val) {
            invalid_index = i as i32;
        }
    });

    invalid_index
}

fn calculate_diff_vec(t: &[i32], ignore_index: i32) -> Vec<i32> {
    let mut ret: Vec<i32> = vec![];
    let mut start_index = 1_usize;
    let mut prev = t[0];

    if ignore_index == 0 {
        start_index = 2;
        prev = t[1]
    }

    for (i, v) in t.iter().enumerate().skip(start_index) {
        if i == ignore_index as usize {
            continue;
        }

        let current: i32 = *v;
        let diff = current - prev;
        prev = current;
        ret.push(diff);
    }

    ret
}

pub fn run(data: &str) {
    let lines = data.split('\n');

    let mut safe_reports = 0;
    for line in lines {
        let t: Vec<i32> = line.split(" ").map(|v| v.parse::<i32>().unwrap()).collect();
        let diff_vec = calculate_diff_vec(&t, -1);
        if check_diff_vec(&diff_vec) == -1 {
            safe_reports += 1
        };
    }

    println!("{}", safe_reports)
}
