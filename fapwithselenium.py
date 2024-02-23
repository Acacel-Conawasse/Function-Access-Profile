import pyautogui
import csv
import time

# Function to perform mouse click at specified coordinates
def mouse_click(x, y):
    pyautogui.click(x, y)

# Function to automate settings based on a row from the settings.txt
def automate_settings(row, initial_x, initial_y):
    # Reset to the starting point for each setting
    mouse_click(initial_x, initial_y)
    
    # Process each setting based on its index
    for index, setting in enumerate(row):
        print(f"Processing setting at index {index}: {setting}")  # Print the current setting being processed

        # Manager - Department Manager
        if index == 0:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=20, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=21, interval=0.07)
                pyautogui.press('up')  # Assuming <up> to disallow
                pass
        # Dataviews - Group Edits
        elif index == 1:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=23, interval=0.07)
                pyautogui.press('enter')
                pass

        # Group approval of timecards
        elif index == 2:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=38, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=41, interval=0.07)
                pass
        # Add
        elif index == 3:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=43, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
            
        # Remove
        elif index == 4:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=45, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
        #Remove All
        elif index == 5:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=47, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
		#Edit data after non account approval by self
        elif index == 6:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=49, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
		#Edit data after non account approval by others
        elif index == 7:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=51, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
		#Comments in Dataviews
        elif index == 8:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=53, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
		#Notes for comments in Dataviews
        elif index == 9:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=55, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
		#Filter by Selected Job Seniority
        elif index == 10:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=59, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
		#Pay code edits in Dataviews
        elif index == 11:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=61, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('down')
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
		#Mark Exceptions as Reviewed
        elif index == 12:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=38, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=38, interval=0.07)
                pyautogui.press('enter')
                pass
        #Pay from Schedule in Dataviews
        elif index == 13:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=55, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=58, interval=0.07)
                pass    
		#Start Pay from Schedule
        elif index == 14:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=60, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass 
		#Stop Pay from Schedule
        elif index == 15:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=62, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass    
		#Punch edits in Dataviews#
        elif index == 16:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=55, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=55, interval=0.07)
                pyautogui.press('enter')
                pass 
        #Sign-off in Dataviews        
        elif index == 17:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=60, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=63, interval=0.07)
                pass
        #Add        
        elif index == 18:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=65, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  
        #Remove            
        elif index == 19:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=60, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=60, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
        #Transfers in Dataviews
        elif index == 20:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=63, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=66, interval=0.07)
                pass    #Open
        #Perform labor category transfers
        elif index == 21:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=68, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  
        #Perform cost center transfers
        elif index == 22:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=70, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  
        #Perform work rule transfers
        elif index == 23:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=72, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  
        #Perform job transfers
        elif index == 24:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=84, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  
        #Start Time on pay code edits
        elif index == 25:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=23, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=23, interval=0.07)
                pyautogui.press('enter')
                pass    #Close


        #Scheduling
        elif index == 26:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=26, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=29, interval=0.07)
                pass    #Open
        #Open Shift Available Notification
        elif index == 27:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=32, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)
                pass  
        #Schedule access
        elif index == 28:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=34, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass
            
        #Filter Location by Employee Group
        elif index == 29:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=36, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pyautogui.press('enter')
                pass
        
        #Schedule Views
        elif index == 30:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=39, interval=0.07)
                pass    #Open   
		#	Employment Term View of Schedule
        elif index == 31:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=41, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass    
		#	Employee View of Schedule
        elif index == 32:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=43, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#	Group View of Schedule
        elif index == 33:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=45, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#	Job View of Schedule
        elif index == 34:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=47, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#	Display Location-based Add-on Data when Employee Group Filtering Enabled
        elif index == 35:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=49, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#	Run reports within Schedule Planner
        elif index == 36:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=51, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#	Pay Code Comments in Schedules
        elif index == 37:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=53, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#	Notes for Pay Code Comments in Schedules
        elif index == 38:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=36, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=36, interval=0.07)
                pyautogui.press('enter')
                pass   
        #Schedule Quick Actions 50 tabs 
        elif index == 39:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=50, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=53, interval=0.07)
                pass    #Open    
        #Add segment tag
        elif index == 40:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=55, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Schedule pay code edits
        elif index == 41:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=61, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #View audit trails in Schedules
        elif index == 42:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=63, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Filter audit trails in Schedules
        elif index == 43:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=50, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=50, interval=0.07)
                pyautogui.press('enter')
                pass    #Close 

        #Transfers in Schedules
        elif index == 44:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=63, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=66, interval=0.07)
                pass    #Open
        #Perform labor category transfers
        elif index == 45:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=68, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular    
        #Perform cost center transfers
        elif index == 46:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=70, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Perform work rule transfers
        elif index == 47:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=72, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Perform job transfers
        elif index == 48:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=74, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Schedule Shift Comments
        elif index == 49:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=76, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Notes for Schedule Shift Comments
        elif index == 50:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=78, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Mark Schedule Posted
        elif index == 51:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=84, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Mark Schedule Unposted
        elif index == 52:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=86, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Availability
        elif index == 53:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=63, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=63, interval=0.07)
                pyautogui.press('enter')
                pass    #Close




        #Workload Planner 76
        elif index == 54:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=76, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=79, interval=0.07)
                pass    #Open
        #Budget Pattern
        #Budget Calendar
        #Plan Pattern
        #Plan Calendar
        #Budget Volume
        #Plan Volume
        #Actual Volume
        #Actual Calendar
        #Generate Workload
        #Lock Volume
        #Run Priority Scheduling Engine
        #Run Schedule Engine
        #Schedule Day Lock
            #5 Tabs to Shift Profile sets <Edit> 
            #6 Tabs to Shift Profile Sets <view> 
        #Shift Profile Sets
            #4 Tabs to Shift Profile <Edit> 
            #5 Tabs to Shift Profile <view> 
        #Shift Profiles
            #4 Tabs to Enter Time Off 
        #Enter Time Off
            #6 Tabs to Pay Code Edits using Pattern Day
        #Pay Code Edits using Pattern Day
            #8 Tabs to Add to schedule Group 
        #Add to Schedule Group
        #Remove from Schedule Group
        #Edit Group Schedules
        #Lock Shifts
        #Assign Breaks
        #Team Definition Setup
        #Team Definition Setup Extended Access
            #4 Tabs to replace shift
        #Replace shift
        #Append shift
        #Insert transfer <Two Tabs to Employee visibility period and enter> Not closing any Drops 
            
        #Employee Visibility Periods
        #Request Submission Control
        #Request Period Extended Access
        #Recurrent / Rolling periods
        #Multi-Group options
        #Employee Priority option
        #Personal Hyperfinds for Employee Query
        #Visibility Period Actions
        #Call Log
        #Call List
        #Group Edit Results
        #Calendar views for Managers <Closing Scheduling with initial click and 26 Tabs> 

        #Timecard Editor for Managers
        #Timecard access
        #Allow negatives in Timecard Editor
        #Approval in Timecard Editor
        #Add
        #Remove
        #Remove All
        #Edit data after non account approval by self
        #Edit data after non account approval by others
        #Cancel meal deductions in Timecard Editor
        #Comments in Timecard Editor


        # Delay to avoid sending inputs too quickly
        time.sleep(0.5)

# Read settings.txt and apply settings
def main():
    initial_x, initial_y = -1166, -215  # Update these values to the initial click position
    with open('settings.txt', mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip the header row
        for row in reader:
            automate_settings(row, initial_x, initial_y)
            time.sleep(3)  # Delay between processing each row

if __name__ == "__main__":
    main()
