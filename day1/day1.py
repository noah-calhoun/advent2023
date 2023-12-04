# Something is wrong with global snow production, 
#   and you've been selected to take a look. The Elves have even given you a map; on it, 
#   they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; 
#   the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you 
#   ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky 
#   ("of course, where do you think snow comes from") 
#   when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) 
#   has been amended by a very young Elf who was apparently just excited to show off her art skills. 
#   Consequently, the Elves are having trouble reading the values on the document.
# The newly-improved calibration document consists of lines of text; 
#   each line originally contained a specific calibration value that the Elves now need to recover. 
#   On each line, the calibration value can be found by combining the first digit and the last digit 
#   (in that order) to form a single two-digit number.


def main():    
    file = open('day1.txt', 'r')
    lines = file.readlines()
    cumulative = 0
    forward = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six":"6", "seven":"7", "eight": "8", "nine":"9"}
    backward = {"eno": "1", "owt": "2", "eerht": "3", "ruof": "4", "evif": "5", "xis": "6", "neves": "7", "thgie": "8", "enin": "9"}
    for line in lines:
        first = ""
        last = ""
        left_current = ""
        right_current = ""
        i, j = 0, len(line) -1
        while first == "" or last == "":
            left = line[i]
            right = line[j]

            if first == "": 
                if left.isalpha():
                    left_current += left
                    for word in forward:
                        if word in left_current:
                            first = forward[word]
                            break
                elif left.isdigit():
                    first = left

            if last == "":
                if right.isalpha():
                    right_current += right
                    for word in backward:
                        if word in right_current:
                            last = backward[word]
                            break
                elif right.isdigit():
                    last = right
            i += 1
            j -= 1

        cumulative += int(first + last)            

    return cumulative

if __name__ == '__main__':
    print(main())