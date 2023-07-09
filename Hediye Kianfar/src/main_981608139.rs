pub fn is_prime(n: u32) -> bool {
    if n <= 1 {
        return false;
    }

    for i in 2..(n / 2 + 1) {
        if n % i == 0 {
            return false;
        }
    }

    true
}

#[allow(dead_code)]
fn main() {
    println!("{}", is_prime(23));
}