participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]

scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]

qualification_score = 70
distinction_score = 90

print("="*50)

# Make sure the lists have the same number of elements
if len(participants) != len(scores):
    print("Error: The lists donot have the same number of elements!")
else:
    print("The lists have the same number of elements, continue the operation.")

print("="*50)

# First, display all the current participants with their scores. Use zip()
print("Current Participants List:")
for name, score in zip(participants, scores):
    print(f"{name}: {score} scores")
print("="*50)

# Write the logic to accept a new participant's name and their score. 
# While entering, also check if they are already in the list of participants. 
# If the participant is already registered, display a message and do not add them to the list.
# If the name is empty, then print an error saying that the name cannot be empty, and don't add them to the list.
# If the score is not a number, then print an error saying that the score must be a number, and don't add them to the list.
# If the score is less than 0 or greater than 100, then print an error saying that the score must be between 0 and 100, and don't add them to the list.
# Otherwise, add the participant and their score to the lists and display a message saying that they have been successfully registered.
print("Accept a new participant's name and their score")
new_name = input("Please enter the participant's name: ").strip()
new_score_input = input("Please enter the score: ").strip()

if new_name == "":
    print("Error: Name cannot be empty!")
else:
    already_registered = False
    for name in participants:
        if name.lower() == new_name.lower():
            already_registered = True
            break
    
    if already_registered:
        print(f"Error: {new_name} is already registered!")
    else:
        is_valid_number = True
        decimal_count = 0
        
        for ch in new_score_input:
            if ch == '.':
                decimal_count = decimal_count + 1
                if decimal_count > 1:
                    is_valid_number = False
                    break
            elif ch < '0' or ch > '9':
                is_valid_number = False
                break
        
        if not is_valid_number or new_score_input == "":
            print("Error: Score must be a valid number!")
        else:
            if '.' in new_score_input:
                parts = new_score_input.split('.')
                whole_part = parts[0]
                decimal_part = parts[1]
                
                whole_value = 0
                for ch in whole_part:
                    digit = 0
                    if ch == '0':
                        digit = 0
                    elif ch == '1':
                        digit = 1
                    elif ch == '2':
                        digit = 2
                    elif ch == '3':
                        digit = 3
                    elif ch == '4':
                        digit = 4
                    elif ch == '5':
                        digit = 5
                    elif ch == '6':
                        digit = 6
                    elif ch == '7':
                        digit = 7
                    elif ch == '8':
                        digit = 8
                    elif ch == '9':
                        digit = 9
                    whole_value = whole_value * 10 + digit
                
                decimal_value = 0
                place = 10
                for ch in decimal_part:
                    digit = 0
                    if ch == '0':
                        digit = 0
                    elif ch == '1':
                        digit = 1
                    elif ch == '2':
                        digit = 2
                    elif ch == '3':
                        digit = 3
                    elif ch == '4':
                        digit = 4
                    elif ch == '5':
                        digit = 5
                    elif ch == '6':
                        digit = 6
                    elif ch == '7':
                        digit = 7
                    elif ch == '8':
                        digit = 8
                    elif ch == '9':
                        digit = 9
                    decimal_value = decimal_value + digit / place
                    place = place * 10
                
                new_score = whole_value + decimal_value
            else:
                new_score = 0
                for ch in new_score_input:
                    digit = 0
                    if ch == '0':
                        digit = 0
                    elif ch == '1':
                        digit = 1
                    elif ch == '2':
                        digit = 2
                    elif ch == '3':
                        digit = 3
                    elif ch == '4':
                        digit = 4
                    elif ch == '5':
                        digit = 5
                    elif ch == '6':
                        digit = 6
                    elif ch == '7':
                        digit = 7
                    elif ch == '8':
                        digit = 8
                    elif ch == '9':
                        digit = 9
                    new_score = new_score * 10 + digit
            
            if new_score < 0 or new_score > 100:
                print("Error: Score must be between 0 and 100!")
            else:
                participants.append(new_name)
                scores.append(new_score)
                print(f"Success! {new_name} has been registered with a score of {new_score}.")

print("="*50)

# Write the logic to search for a specific participant.
# If the participant is found, display their name, score, and whether they are qualified or not.
# If the score is more than the distinction score, display that they have a DISTINCTION.
# If the score is more than the qualification score, display that they are QUALIFIED.
# Otherwise, display that they are NOT QUALIFIED.
# If the participant is not found, display a message saying that they are not found.
print("Search for a specific participant")
search_name = input("Please enter the participant's name to search for: ").strip()

found = False
for i in range(len(participants)):
    if participants[i].lower() == search_name.lower():
        found = True
        score = scores[i]
        print(f"\nFound participant: {participants[i]}")
        print(f"Score: {score}")

        if score > distinction_score:
            print("Status: DISTINCTION (Excellent)")
        elif score > qualification_score:
            print("Status: QUALIFIED (Qualified)")
        else:
            print("Status: NOT QUALIFIED (Not Qualified)")
        break

if not found:
    print(f"Error: Participant {search_name} not found.")

print("="*50)

# Display every participant's name, score, and whether they are qualified or not. 
print("Every participant's information")
for i in range(len(participants)):
    name = participants[i]
    score = scores[i]
    
    if score > distinction_score:
        status = "DISTINCTION"
    elif score > qualification_score:
        status = "QUALIFIED"
    else:
        status = "NOT QUALIFIED"
    
    print(f"{name}: {score} scores - {status}")

print("="*50)

# Write the logic to find if there's even one participant that has a distinction, and if all the participants have passed (i.e., scored 50 or more).
has_distinction = False
all_passed = True

for i in range(len(scores)):
    if scores[i] > distinction_score:
        has_distinction = True
    if scores[i] < 50:
        all_passed = False

print("Statistics Check")
print(f"Whether there is at least one participant with a distinction (>90 points): {has_distinction}")
print(f"Whether all participants have passed (>=50 points): {all_passed}")

print("="*50)

# Write the logic to update a participant's score.
# Ensure that the participant exists in the list before updating their score. 
# Also ensure that the new score is a valid number between 0 and 100.
print("Update Score")
update_name = input("Please enter the participant's name to update: ").strip()

found_index = -1
for i in range(len(participants)):
    if participants[i].lower() == update_name.lower():
        found_index = i
        break

if found_index == -1:
    print(f"Error: Participant '{update_name}' not found.")
else:
    new_score_input = input(f"Enter new score for {participants[found_index]}: ").strip()
    
    is_valid_number = True
    decimal_count = 0
    
    for ch in new_score_input:
        if ch == '.':
            decimal_count = decimal_count + 1
            if decimal_count > 1:
                is_valid_number = False
                break
        elif ch < '0' or ch > '9':
            is_valid_number = False
            break
    
    if not is_valid_number or new_score_input == "":
        print("Error: Score must be a valid number!")
    else:
        if '.' in new_score_input:
            parts = new_score_input.split('.')
            whole_part = parts[0]
            decimal_part = parts[1]
            
            whole_value = 0
            for ch in whole_part:
                digit = 0
                if ch == '0':
                    digit = 0
                elif ch == '1':
                    digit = 1
                elif ch == '2':
                    digit = 2
                elif ch == '3':
                    digit = 3
                elif ch == '4':
                    digit = 4
                elif ch == '5':
                    digit = 5
                elif ch == '6':
                    digit = 6
                elif ch == '7':
                    digit = 7
                elif ch == '8':
                    digit = 8
                elif ch == '9':
                    digit = 9
                whole_value = whole_value * 10 + digit
            
            decimal_value = 0
            place = 10
            for ch in decimal_part:
                digit = 0
                if ch == '0':
                    digit = 0
                elif ch == '1':
                    digit = 1
                elif ch == '2':
                    digit = 2
                elif ch == '3':
                    digit = 3
                elif ch == '4':
                    digit = 4
                elif ch == '5':
                    digit = 5
                elif ch == '6':
                    digit = 6
                elif ch == '7':
                    digit = 7
                elif ch == '8':
                    digit = 8
                elif ch == '9':
                    digit = 9
                decimal_value = decimal_value + digit / place
                place = place * 10
            
            new_score = whole_value + decimal_value
        else:
            new_score = 0
            for ch in new_score_input:
                digit = 0
                if ch == '0':
                    digit = 0
                elif ch == '1':
                    digit = 1
                elif ch == '2':
                    digit = 2
                elif ch == '3':
                    digit = 3
                elif ch == '4':
                    digit = 4
                elif ch == '5':
                    digit = 5
                elif ch == '6':
                    digit = 6
                elif ch == '7':
                    digit = 7
                elif ch == '8':
                    digit = 8
                elif ch == '9':
                    digit = 9
                new_score = new_score * 10 + digit
        
        if new_score < 0 or new_score > 100:
            print("Error: Score must be between 0 and 100!")
        else:
            old_score = scores[found_index]
            scores[found_index] = new_score
            print(f"Success! {participants[found_index]}'s score updated from {old_score} to {new_score}.")

print("="*50)

# Write the logic to withdraw (remove) a participant from the list.
# Ensure that the score for that specific participant is also removed from the scores list
print("Remove Participant")
remove_name = input("Please enter the participant's name to remove: ").strip()

found_index = -1
for i in range(len(participants)):
    if participants[i].lower() == remove_name.lower():
        found_index = i
        break

if found_index == -1:
    print(f"Error: Participant {remove_name} not found.")
else:
    removed_name = participants[found_index]
    removed_score = scores[found_index]
    
    participants.pop(found_index)
    scores.pop(found_index)
    
    print(f"Success! {removed_name} (Score: {removed_score}) has been removed.")

print("="*50)

# Create and display a scoreboard where all the participants and their scores are displayed in descending order.
# Display their rank alongside the participant name and score
print("Scoreboard")

paired_list = []
for i in range(len(participants)):
    paired_list.append((participants[i], scores[i]))

for i in range(len(paired_list)):
    for j in range(i + 1, len(paired_list)):
        if paired_list[j][1] > paired_list[i][1]:
            temp = paired_list[i]
            paired_list[i] = paired_list[j]
            paired_list[j] = temp

print("Rank\tName\t\tScore")
print("-" * 35)
for i in range(len(paired_list)):
    rank = i + 1
    name = paired_list[i][0]
    score = paired_list[i][1]
    
    if len(name) < 8:
        print(f"{rank}\t{name}\t\t{score}")
    else:
        print(f"{rank}\t{name}\t{score}")

print("="*50)

# Calculate statistics: 
# Calculate what the highest score is, what lowest score is, what the average score is.
# Calculate how many participants have the highest score and the lowest score
# Calculate how many participants have distinctions, how many are qualified, and how many are not qualified
print("Calculate statistics")

if len(scores) > 0:
    highest_score = scores[0]
    lowest_score = scores[0]
    total_score = 0
    
    for score in scores:
        if score > highest_score:
            highest_score = score
        if score < lowest_score:
            lowest_score = score
        total_score = total_score + score
    
    average_score = total_score / len(scores)
    
    highest_count = 0
    lowest_count = 0
    for score in scores:
        if score == highest_score:
            highest_count = highest_count + 1
        if score == lowest_score:
            lowest_count = lowest_count + 1
    
    distinction_count = 0
    qualified_count = 0
    not_qualified_count = 0
    
    for score in scores:
        if score > distinction_score:
            distinction_count = distinction_count + 1
        elif score > qualification_score:
            qualified_count = qualified_count + 1
        else:
            not_qualified_count = not_qualified_count + 1
    
    print(f"Highest Score: {highest_score} points ({highest_count} participants achieved)")
    print(f"Lowest Score: {lowest_score} points ({lowest_count} participants achieved)")
    print(f"Average Score: {average_score:.2f} points")
    print(f"\nDistinctions (>{distinction_score} points): {distinction_count} participants")
    print(f"Qualifications (>{qualification_score} points): {qualified_count} participants")
    print(f"Not Qualified: {not_qualified_count} participants")
else:
    print("The list is empty, unable to calculate statistical data.")

print("="*50)

# Generate a final report that displays the participant name, their rank, their score, and their qualification (DISTINCTION, QUALIFIED, NOT QUALIFIED)
# Also the display all the statistics you calculated above
print("Final Report")
print("=" * 50)

print("Participant Performance Report")
print("-" * 50)
print("Rank\tName\t\tScore\t\tQualification")
print("-" * 50)

for i in range(len(paired_list)):
    rank = i + 1
    name = paired_list[i][0]
    score = paired_list[i][1]
    
    if score > distinction_score:
        status = "DISTINCTION"
    elif score > qualification_score:
        status = "QUALIFIED"
    else:
        status = "NOT QUALIFIED"
    
    if len(name) < 8:
        print(f"{rank}\t{name}\t\t{score}\t\t{status}")
    else:
        print(f"{rank}\t{name}\t{score}\t\t{status}")

print("Statistical Summary")
if len(scores) > 0:
    print(f"Total Participants: {len(scores)}")
    print(f"Highest Score: {highest_score} points")
    print(f"Lowest Score: {lowest_score} points")
    print(f"Average Score: {average_score:.2f} points")
    print(f"Distinction Holders: {distinction_count}")
    print(f"Qualified Participants: {qualified_count}")
    print(f"Not Qualified Participants: {not_qualified_count}")
print("=" * 50)