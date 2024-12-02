pub fn run(data: &str) {
    let lines = data.split('\n');

    let mut safe_reports = 0;
    for line in lines {
        let t: Vec<&str> = line.split(" ").collect();
        let mut ascending = true;
        if t[1].parse::<i32>().unwrap() - t[0].parse::<i32>().unwrap() < 0 {
            ascending = false
        }

        let mut prev: i32 = t[0].parse().unwrap();
        let mut is_safe = true;
        for (index, v) in t.iter().enumerate() {
            if index == 0 {
                continue;
            }
            let current: i32 = v.parse().unwrap();
            match ascending {
                true => {
                    let diff = current - prev;
                    if !(1..=3).contains(&diff) {
                        is_safe = false;
                        break;
                    }
                }
                false => {
                    let diff = prev - current;
                    if !(1..=3).contains(&diff) {
                        is_safe = false;
                        break;
                    }
                }
            };

            prev = current;
        }
        if is_safe {
            safe_reports += 1;
        }
    }

    println!("{}", safe_reports)
}
