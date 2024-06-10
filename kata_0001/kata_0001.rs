
fn main() {
    let mut input = String::new();
    let _ = std::io::stdin().read_line(&mut input);
    let values: Vec<&str> = input.trim().split(',').collect();
    let mut hex_color = String::from("#");
    for value in values {
        let int_value = u8::from_str_radix(value.trim(), 10);
        hex_color.push_str(format!("{:02X}", int_value.unwrap()).as_str());
    }
    println!("hex color : {}", hex_color);
}
