pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::any::type_name;

    #[test]
    fn test_add_result() {
        assert_eq!(add(1, 2), 3);
    }

    fn type_of<T>(_: T) -> &'static str {
        type_name::<T>()
    }

    #[test]
    fn test_add_type() {
        assert_eq!(type_of(add(1, 2)), type_name::<i32>());
    }
}
