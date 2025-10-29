from metaflow import FlowSpec, step

class TestFlow1(FlowSpec):
    """A basic, linear flow with variable manipulation."""

    @step
    def start(self):
        """Initialize the flow and a variable."""
        print("Starting the flow")
        self.variable = 42
        self.variable_list = [self.variable]
        self.next(self.step_addition)

    @step
    def step_addition(self):
        """Adds a number to the variable."""
        print("Step Addition")
        self.variable += 10
        self.variable_list.append(self.variable)
        self.next(self.step_multiplication)

    @step
    def step_multiplication(self):
        """Multiplies the variable by a number."""
        print("Step Multiplication")
        self.variable *= 2
        self.variable_list.append(self.variable)
        self.next(self.step_division)
        
    @step
    def step_division(self):
        """Divides the variable by a number"""
        print("Step Division")
        self.variable /= 4
        self.variable_list.append(self.variable)
        self.next(self.end)

    @step
    def end(self):
        """Prints the final variable and list."""
        print("Ending the flow")
        print(f"Final variable: {self.variable}")
        print(f"Variable list: {self.variable_list}")

if __name__ == "__main__":
    TestFlow1()
