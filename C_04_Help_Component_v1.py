from tkinter import *
from functools import partial # To prevent unwanted windows


#  Classes start here
class StartGame:
    """
    Initial Game inter-face (asks users how many rounds they would like to play)
    """

    def __init__(self):
        """
        Gets number of rounds from user
        """

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()


        self.play_button = Button(self.start_frame, font=("Arial", 16, "bold"),
                                  fg="#FFFFFF", bg="#0057D8", text="Play", width=10,
                                  command=self.check_rounds)
        self.play_button.grid(row=0, column=1)

    def check_rounds(self):
        """
         Checks users have entered 1 or more rounds
        """

        # Retrieve temperature to be converted
        rounds_wanted = 5
        self.to_play(rounds_wanted)

    def to_play(self, num_rounds):
        """
        Invokes Game GUI and takes across number of rounds to be played.
        """
        Play(num_rounds)
        # Hide root window (ie: hide rounds choice window).
        root.withdraw()


class Play:
    """
    Interface for playing the Colour Quest Game
    """

    def __init__(self, how_many):
        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        self.heading_label = Label(self.game_frame, text="Colour Quest", font=("Arial", 16, "bold"),
                                   padx=5, pady=5)
        self.heading_label.grid(row=0)

        self.to_hints_button =Button(self.game_frame, font=("Arial", 14, "bold"),
                                  text="Hints", width=15, fg="#FFFFFF",
                                  bg="#FF8000", padx=10, pady=10, command=self.to_hints)
        self.to_hints_button.grid(row=1)

    def to_hints(self):
        """
        Displays hints for playing game
        :return:
        """
        DisplayHints(self)


class DisplayHints:
    """
    Displays hints for Colour Quest Game
    """

    def __init__(self, partner):

        # setup dialogue box and background colour
        background = "#ffe6cc"
        self.hints_box = Toplevel()

        # disable hints button
        partner.to_hints_button.config(state=DISABLED)

        # If users press cross at top, closes hints and
        # 'releases' hints_button
        self.hints_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_hints, partner))
        self.hints_frame = Frame(self.hints_box, width=300,
                                height=200)
        self.hints_frame.grid()

        self.hints_heading_label = Label(self.hints_frame,
                                        text="Hints",
                                        font=("Arial", 14, "bold"))
        self.hints_heading_label.grid(row=0)

        hints_text =("The score for each colour relates to it's hexadecimal code. \n\n "
                     "Remember, the hex code for white is #FFFFFF - which is the best possible "
                     "score. \n\n "
                     "The hex code for black is #000000 which is the worst possible score. \n\n "
                     "The first colour in the code is red, so if you had to choose between "
                     "red (#FF0000), green(#00FF00) and blue (#0000FF), then red would be the "
                     "best choice. \n\n "
                     "Good luck ")

        self.hints_text_label = Label(self.hints_frame,
                                     text=hints_text, wraplength=350,
                                     justify="left")
        self.hints_text_label.grid(row=1,pady=10)

        self.dismiss_button = Button(self.hints_frame,
                                     font=("Arial", 12, "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_hints, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # List and loop to set background colour on
        # everything except the buttons.
        recolour_list = [self.hints_frame, self.hints_heading_label,
                         self.hints_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_hints(self, partner):
        """
        Closes hints dialogue box (and enables hints button)
        """
        # Put hints button back to normal...
        partner.to_hints_button.config(state=NORMAL)
        self.hints_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    StartGame()
    root.mainloop()


