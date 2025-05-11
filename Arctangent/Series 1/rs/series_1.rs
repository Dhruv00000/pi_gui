use std::time::{Duration, Instant};
use std::io::{self, Write};

fn main() {

    let mut iterator: u16 = 1;
    let mut approximation: f64 = 0.0;
    let mut previous_approximation: f64 = 0.0;
    let mut deviation: f64;
    let mut final_accuracy: u8 = 0;
    let mut start_time: Instant;
    let mut iteration_time: Duration;
    let mut a_first: f64 = f64::powf(2.0, 1.0/2.0);
    let mut a_second: f64 = f64::powf(a_first + 2.0, 1.0/2.0);
    let mut total_computation_time: Duration = Duration::from_secs(0); // Duration::from_secs(0) is just a temporary value in order to initialize the total_computation_time variable.

    let mut input: String = String::new();
    print!("\nEnter a value of the starting index: ");
    io::stdout().flush().expect("flushed");
    match io::stdin().read_line(&mut input) {
        Ok(_) => {
            match input.trim().parse::<u16>() {

                Ok(starting_index) => { 

                    let mut i: u16 = 2;
                    while i < starting_index { // Perform the recursion for a_n until we reach the required starting value entered by the user.
                        a_first = a_second;
                        a_second = continue_recursion(a_second);

                        i += 1;
                    }

                    let flag: bool = starting_index >= 2 && starting_index < 28; // After 26 steps of the recursion, a_26 becomes close enough to 2 in the floating point system for arctan(2 - a_26) to become zero, which is our numerator. Therefore, from a_26 onwards, all values of a_k tend close enough to 2 to make the approximation zero for all iterations, creating an infinite loop.
                    if flag {
                        loop {
    
                            start_time = Instant::now();
                            approximation += f64::powf(2.0, starting_index as f64) * (f64::powf(2.0 - a_first, 1.0/2.0) / a_second).atan();
                            a_first = a_second;
                            a_second = continue_recursion(a_second);
                            iteration_time = start_time.elapsed(); // only the mathematical computations are considered in the total computation time, and everything else like calculating the deviation and accuracy is not considered.

                            println!("\nIteration {}", iterator);
                            println!("Approximation = {:.51}", approximation);
                    
                            let mut i: u8 = 0;
                            for c in String::from("3.141592653589793238462643383279502884197169399375105").chars() {
                                if c != match approximation.to_string().chars().nth(i as usize) {
                                    Some(c2) => c2,
                                    None => char::from(0)
                                } {
                                    if i < 2 { println!("No accurate decimal places.") }
                                    else {
                                        println!("{} correct decimal place(s)", i - 2);
                                        final_accuracy = i - 2;
                                    }
                                    break;
                                }
                    
                                i += 1;
                            }
                    
                            println!("Iteration duration: {:?}", iteration_time);
                            total_computation_time += iteration_time;
                        
                            deviation = approximation - previous_approximation;
                            if deviation.abs() < 1e-50 {
                                println!("\nSummation converged. Terminating program...");
                                break;
                            }
                            else { println!("Deviation from previous iteration: {:.51}\n", deviation) }
                    
                            previous_approximation = approximation;
                            iterator += 1;

                        }

                        println!("Computed {} correct decimal places in {:?} and {} iterations.\n", final_accuracy, total_computation_time, iterator);
                    }
                    else { println!("\nPlease enter a number in the range 2 to 27 (both inclusive).\n"); }

                 },

                Err(_) => { println!("\nPlease enter a positive base-10 integer.\n"); }

            }
        },
        Err(e) => print!("{}", e)
    }

}

fn continue_recursion(second: f64) -> f64 { return f64::powf(second + 2.0, 1.0/2.0); }