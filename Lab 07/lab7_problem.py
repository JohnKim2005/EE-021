"""
Lab 7 code template
"""


class Resistor:
    """This is a class for a resistor object.
    """
    def __init__(self, resistance=None, colors=None):
        self.resistance = resistance  # resistance value in ohms
        self.colors = colors  # list of three colors for the resistor
        self.multimeter_range = None  # range of the multimeter needed

    def get_multimeter_range(self):
        """Function to get multimeter range needed to measure the resistance

        Returns:
            int: The range is returned.
        """
        multimeter_range_available = [200, 2*10**3, 20*10**3,
                                      200*10**3, 2*10**6]
        ######################################################################
        # Write code to determine the multimeter range needed 
        # to measure the resistance
        # Store this value in the variable self.multimeter_range
        # You are not allowed to change any pre-written part of the code
        # Write your code below this line

        ######################################################################
        print("Measure this resistor with a multimeter"
              " that has a range of", self.multimeter_range)
        return self.multimeter_range

    def get_resistance(self):
        """Class method to get the resistance value of the resistor

        Returns:
            int or float: The resistance value
        """
        return self.resistance

    def set_resistance(self, resistance=None, colors=None):
        """Set the resistance value either using resistance or colors

        Args:
            resistance (float, optional): The value for resistance.
            colors (list, optional): List of colors for resistor.

        Raises:
            ValueError: If both resistance and colors are None.
            ValueError: If both resistance and colors are provided.
            ValueError: If colors is not a list or not of length 3.

        Returns:
            int/float: Resistance value that was set
        """
        # Error checking for the input in this method (don't change)
        if colors is None and resistance is None:
            raise ValueError("Either resistance or colors must be provided")
        if resistance is not None:
            if colors is not None:
                raise ValueError("Either resistance or colors, not both")
            self.resistance = resistance
            return self.resistance
        if type(colors) is not list or len(colors) != 3:
            raise ValueError("Colors must be a list of three elements")
        self.colors = colors
        ######################################################################
        # Define a dictionary of color values here with keys as color names
        # and values as digits
        # Use https://resistorcolorcodecalc.com/ to find out values for
        # different colors.
        # For example, black is 0, brown is 1, and so on.
        color_values = {

        }
        ######################################################################

        ######################################################################
        # Write code here to use the dictionary to compute the resistance
        # Store the value in the variable self.resistance
        # You are not allowed to change any pre-written part of the code
        # Write your code below this line

        #######################################################################
        return self.resistance


class Series:
    """Class for series resistors
    """
    def __init__(self, resistors):
        self.resistors = resistors

    def get_resistance(self):
        """Method to get the total resistance of the series resistors

        Returns:
            int/float: Series resistance value
        """
        total_resistance = 0
        #########################################################################
        # Write code here to compute the total resistance of the series resistors
        # Store the value in the variable total_resistance
        # You are not allowed to change any pre-written part of the code
        # Write your code below this line

        #########################################################################
        return total_resistance


class Parallel:
    """Parallel resistors class
    """
    def __init__(self, resistors):
        self.resistors = resistors

    def get_resistance(self):
        """Method to get the total resistance of the parallel resistors

        Returns:
            int/float: Parallel resistance value
        """
        total_resistance = 0
        ###########################################################################
        # Write code here to compute the total resistance of the parallel resistors
        # Store the value in the variable total_resistance
        # You are not allowed to change any pre-written part of the code
        # Write your code below this line

        ###########################################################################
        return total_resistance


if __name__ == "__main__":
    resistor_1 = Resistor(1000)
    resistor_1.get_multimeter_range()
    r_1 = resistor_1.get_resistance()
    ###################################################################
    # Create a second resistor object with resistance value initialized
    # you may choose the value for resistor 2.
    resistor_2 = None # replace None with your actual code.
    # Update resistance 2 value to a different value 
    # using the set_resistance method, 
    # and store the value in r2
    r_2 = None  # replace None with your actual code.
    print("Resistor 2 is now", r_2, "ohms.")
    ###################################################################

    series_resistor = Series([resistor_1, resistor_2])
    parallel_resistor = Parallel([resistor_1, resistor_2])
    print(f'Resistors {r_1} and {r_2} in series is: '
          f'{series_resistor.get_resistance()}')
    print(f'Resistors {r_1} and {r_2} in parallel is: '
          f'{parallel_resistor.get_resistance()}')

    # Add one more resistor
    resistor_3 = Resistor(330)
    #########################################################
    # Update resistor 3 values, this time with colors
    # you may choose three colors for resistor 3
    # pass the three colors as a list to the set_resistance method
    # in the set_resistance method, and store the value in r3
    r_3 = None  # replace None with your actual code.
    print("Resistor 3 is now", r_3, "ohms.")
    #########################################################
    resistor_3.get_multimeter_range()
    # Compute series resistance:
    series_resistor = Series([resistor_1, resistor_2, resistor_3])
    # Computer parallel resistance:
    parallel_resistor = Parallel([resistor_1, resistor_2, resistor_3])
    print(f'Resistors {r_1}, {r_2}, and {r_3} in series is: '
          f'{series_resistor.get_resistance():6d}')
    print(f'Resistors {r_1}, {r_2}, and {r_3} in parallel is: '
          f'{parallel_resistor.get_resistance():.2f}')
