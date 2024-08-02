class Student:
    def __init__(self, roll_number, marks):
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

def take_inputs_and_store(filename):
    
    with open(filename, 'w') as file:
        
        for _ in range(5):
            number = input("Enter a number: ")
            file.write(number + "\n")
    print(f"Numbers have been written to {filename}")

def process_file(filename):
    total_sum = 0
    max_number = None
    count_numbers = 0
    marks = []

    
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            marks.append(number)
            total_sum += number
            if max_number is None or number > max_number:
                max_number = number
            count_numbers += 1

    return total_sum, max_number, count_numbers, marks


def main():
    filename = "Shubham_3018.txt"
    take_inputs_and_store(filename)
    
    total_sum, max_number, count_numbers, marks = process_file(filename)
    print(f"Sum of all numbers: {total_sum}")
    print(f"Maximum number: {max_number}")
    print(f"Total count of numbers: {count_numbers}")

    
    roll_number = "YourRollNumber"  
    student = Student(roll_number, marks)

    
    student.display()

if __name__ == "__main__":
    main()
