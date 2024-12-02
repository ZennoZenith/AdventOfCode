fn check_diff_vec(diff_vec: &[i32], ascending: bool) -> bool {
    let mut is_valid = true;
    match ascending {
        true => diff_vec.iter().for_each(|v| {
            if !(1..=3).contains(v) {
                is_valid = false;
            }
        }),
        false => diff_vec.iter().for_each(|v| {
            if !(1..=3).contains(&-v) {
                is_valid = false;
            }
        }),
    };
    is_valid
}

pub fn run(data: &str) {
    let lines = data.split('\n');

    let mut safe_reports = 0;
    for line in lines {
        let t: Vec<&str> = line.split(" ").collect();
        let mut diff_vec = Vec::new();
        let mut ascending = true;
        if t[1].parse::<i32>().unwrap() - t[0].parse::<i32>().unwrap() < 0 {
            ascending = false
        }

        let mut prev: i32 = t[0].parse().unwrap();
        let mut is_safe = true;
        let mut last_stand = true;

        (1..t.len()).for_each(|i| {
            let current: i32 = t[i].parse().unwrap();
            let diff = current - prev;
            diff_vec.push(diff);
        });

        // check for ascending
        let state = check_diff_vec(&diff_vec, true);
        // for i in 0..diff_vec.len() {
        //     let state = check_diff_vec(&diff_vec, true);
        // }
        if state {
            safe_reports += 1;
        }
    }

    println!("{}", safe_reports)
}
