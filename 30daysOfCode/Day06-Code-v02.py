# Enter your code here. Read input from STDIN. Print output to STDOUT

# Main Object - Second Step: Contain all Functions
class StringProcessor:
    def __init__(self):
        # Start list of strings
        self.strings = []
    
    def read_input(self, num_strings):
        # Read input strings and store in a list
        for _ in range(num_strings):
            element = input('')
            self.strings.append(element)
        
    def process_string(sel, string):
        # Process a single string and split the characters by indexes even and odd
        even = []
        odd = []
        
        for index, char in enumerate(string):
            if index%2==0:
                even.append(char)
            else:
                odd.append(char)
        return ''.join(even), ''.join(odd)

    def process_all_strings(self):
        # Process all strings and store in a list then print them
        for string in self.strings:
            even_part, odd_part = self.process_string(string)
            print(even_part, odd_part)

# Main Function - First Step: Execute the Program
def main():
    processor = StringProcessor()
    
    num_strings = int(input())
    
    processor.read_input(num_strings)
    
    processor.process_all_strings()
    
# Run the Program if File running is the Main file
if __name__ == "__main__":
    main()
