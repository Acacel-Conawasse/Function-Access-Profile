import pyautogui
import csv
import time

pyautogui.FAILSAFE = True  # Enable failsafe by moving the mouse to the upper left corner


# Function to perform mouse click at specified coordinates
def mouse_click(x, y):
    pyautogui.click(x, y)

# Function to automate settings based on a row from the settings.txt
def automate_settings(row, initial_x, initial_y):
    # Reset to the starting point for each setting
    mouse_click(initial_x, initial_y)
    
    # Process each setting based on its index
    for index, setting in enumerate(row):
        print(f"Processing setting at index {index}: {setting}")  #Print the current setting being processed
##The Kwiggler ####################################################
        ####################################################
        ####################################################
        ####################################################
        #Everyone 
        if index == 0:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=14, interval=0.07)
                pyautogui.press('enter')
                pyautogui.press('tab', presses=15, interval=0.07)
                pyautogui.press('d') #--Disallow 
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=24, interval=0.07)
                pass    #Open
        #Open an online form
        elif index == 1:
            if setting == 'allowed':
                pyautogui.press('a')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=26, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Show Person Number
        elif index == 2:
            if setting == 'allowed':
                pyautogui.press('a')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=14, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=14, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
#End of Everyone Section. 
#-------------------------------------------------------------------------------------------------------------------
#Employee 
        elif index == 3:
             if setting == '':
                #Employee  Mouse Click (-1664,69)
                tab_and_open(17)
                time.sleep(1)
                tabto(18)
                pyautogui.press('d')
                time.sleep(2)
                pass    #Close
        # Time Stamp for Employees
        elif  index == 4:
            if setting == '':
                #Time Stamp for Employees  
                tab_and_open(20)
                time.sleep(1)
                pass
        #Cancel meal deductions in Time Stamp     
        elif  index == 5:
            if setting == '':
                press_tab_and_decide(setting,23)
                # end of Time Stamp for Employees. Closing group    
                tab_and_open(20)
                time.sleep(1)
                pass
        # "Calendar"
        elif  index == 6:
            if setting == '':
                # Calendar  
                tab_and_open(23)
                time.sleep(1)
                pass
        # Calendar views for employees     
        elif  index == 7:
            press_tab_and_decide(setting,26)       
        # Print Schedule    
        elif  index == 8:
            press_tab_and_decide(setting,28)
        # Employee Visibility Periods    
        elif  index == 9:
            press_tab_and_decide(setting,30)
            # end of Calendar. Closing group    
            tab_and_open(23)
            time.sleep(1)
        # Timecard Editor for Employees (My Timecard)    
        elif  index == 10:
            #Timecard Editor for Employees (My Timecard)  
             tab_and_open(30)
             time.sleep(1)
        # Comments in My Timecard - Add     
        elif  index == 11:
            press_tab_and_decide(setting,40)
        # Comments in My Timecard - Delete    
        elif  index == 12:
            press_tab_and_decide(setting,41)
        # Notes for Comments in My Timecard    
        elif  index == 13:
            press_tab_and_decide(setting,43)
        # Hours Worked amount in My Timecard    
        elif  index == 14:
            press_tab_and_decide(setting,45)
        # "Pay Codes in My Timecard - Edit"    
        elif  index == 15:
            #Pay Codes in My TImecard 
            tab_and_open(47)
            time.sleep(1)
            
            #Check pay code - edit field 
            press_tab_and_decide(setting,50)
        # Pay Codes in My Timecard - View    
        elif  index == 16:
            press_tab_and_decide(setting,52)
        # Move Amounts in My Timecard    
        elif  index == 17:
            press_tab_and_decide(setting,54)
            # End of group. Pay Codes in My TImecard (Close)
            tab_and_open(47)
            time.sleep(1)
        # Punch edits in My Timecard    
        elif  index == 18:
            press_tab_and_decide(setting,50)
        # Calculate totals in My Timecard    
        elif  index == 19:
            press_tab_and_decide(setting,55)
        # Totals breakdown in My Timecard    
        elif  index == 20:
            press_tab_and_decide(setting,57)
        # View schedules in My timecard    
        elif  index == 21:
            press_tab_and_decide(setting,61)
        # View the Audit Trail Tab in My Timecard    
        elif  index == 22:
            press_tab_and_decide(setting,73)
            #Timecard Editor for Employees (My Timecard) (close) 
            tab_and_open(30)
            time.sleep(1)
        # Transfers - View transfers    
        elif  index == 23:
            #Transfers 
            tab_and_open(36)
            time.sleep(1)
            press_tab_and_decide(setting,39)  
        # Perform cost center transfers    
        elif  index == 24:
            press_tab_and_decide(setting,41)
        # Perform labor category transfers    
        elif  index == 25:
            press_tab_and_decide(setting,43)
        # Perform work rule transfers    
        elif  index == 26:
            press_tab_and_decide(setting,45)
        # Perform job transfers    
        elif  index == 27:
            press_tab_and_decide(setting,47)
            #Transfers (close)
            tab_and_open(36)
            time.sleep(1)
        # Access to Employee Home Page    
        elif  index == 28:
            press_tab_and_decide(setting,49)
        # Employee access to My Actions list    
        elif  index == 29:
            press_tab_and_decide(setting,51)
        # Location Data
        elif  index == 30:
            #Location Data 
            tab_and_open(53)
            time.sleep(1)
        # View location data    
        elif  index == 31:
            press_tab_and_decide(setting,58)
            #Location Data (close)
            tab_and_open(53)
            time.sleep(1)
        # Enable location schedule    
        elif  index == 32:
            press_tab_and_decide(setting,58)
        # Access unposted schedule    
        elif  index == 33:
            press_tab_and_decide(setting,67)
        # My Requests    
        elif  index == 34:
            press_tab_and_decide(setting,69)
        # Comments & Notes in my request    
        elif  index == 35:
            press_tab_and_decide(setting,74)
        # Impersonation Access    
        elif  index == 36:
            press_tab_and_decide(setting,76)
        # Offline    
        elif  index == 37:
            #Offline 
            tab_and_open(78)
            time.sleep(1)
        # Mobile App Punch    
        elif  index == 38:
            press_tab_and_decide(setting,81) 
            #end of Employee (close)
            tab_and_open(17)
            time.sleep(1)    
#-------------------------------------------------------------------------------------------------------------------
####################################################
####################################################
####################################################
####################################################
####################################################
        # Manager - Department Manager
        elif index == 39:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=20, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=21, interval=0.07)
                pyautogui.press('up')  # Assuming <up> to disallow
                pass
        # Dataviews - Group Edits
        elif index == 40:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=23, interval=0.07)
                pyautogui.press('enter')
                pass
        # Group approval of timecards
        elif index == 41:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=38, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=41, interval=0.07)
                pass
        # Add
        elif index == 42:
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
        elif index == 43:
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
        elif index == 44:
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
        elif index == 45:
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
        elif index == 46:
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
        elif index == 47:
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
        elif index == 48:
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
        elif index == 49:
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
        elif index == 50:
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
        elif index == 51:
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
        elif index == 52:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=55, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=58, interval=0.07)
                pass    
		#Start Pay from Schedule
        elif index == 53:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=60, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass 
		#Stop Pay from Schedule
        elif index == 54:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=62, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass    
		#Punch edits in Dataviews#
        elif index == 55:
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
        elif index == 56:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=60, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=63, interval=0.07)
                pass
        #Add        
        elif index == 57:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=65, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  
        #Remove            
        elif index == 58:
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
        elif index == 59:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=63, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=66, interval=0.07)
                pass    #Open
        #Perform labor category transfers
        elif index == 60:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=68, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  
        #Perform cost center transfers
        elif index == 61:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=70, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  
        #Perform work rule transfers
        elif index == 62:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=72, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  
        #Perform job transfers
        elif index == 63:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=84, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  
        #Start Time on pay code edits
        elif index == 64:
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
        elif index == 65:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=26, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=29, interval=0.07)
                pass    #Open
        #Open Shift Available Notification
        elif index == 66:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=32, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)
                pass  
        #Schedule access
        elif index == 67:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=34, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass 
        #Filter Location by Employee Group
        elif index == 68:
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
        elif index == 69:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=39, interval=0.07)
                pass    #Open   
		#Employment Term View of Schedule
        elif index == 70:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=41, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass    
		#Employee View of Schedule
        elif index == 71:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=43, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#Group View of Schedule
        elif index == 72:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=45, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#Job View of Schedule
        elif index == 73:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=47, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#Display Location-based Add-on Data when Employee Group Filtering Enabled
        elif index == 74:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=49, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#Run reports within Schedule Planner
        elif index == 75:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=51, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#Pay Code Comments in Schedules
        elif index == 76:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=53, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass   
		#Notes for Pay Code Comments in Schedules
        elif index == 77:
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
        elif index == 78:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=50, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=53, interval=0.07)
                pass    #Open    
        #Add segment tag
        elif index == 79:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=55, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Schedule pay code edits
        elif index == 80:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=61, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #View audit trails in Schedules
        elif index == 81:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=63, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Filter audit trails in Schedules
        elif index == 82:
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
        elif index == 83:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=63, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=66, interval=0.07)
                pass    #Open
        #Perform labor category transfers
        elif index == 84:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=68, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular    
        #Perform cost center transfers
        elif index == 85:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=70, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Perform work rule transfers
        elif index == 86:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=72, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Perform job transfers
        elif index == 87:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=74, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Schedule Shift Comments
        elif index == 88:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=76, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Notes for Schedule Shift Comments
        elif index == 89:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=78, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Mark Schedule Posted
        elif index == 90:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=84, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Mark Schedule Unposted
        elif index == 91:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=86, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Availability
        elif index == 92:
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
        elif index == 93:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=76, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=79, interval=0.07)
                pass    #Open
        #Budget Pattern
        elif index == 94:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=82, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=84, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=3, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=84, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
        #Budget Calendar
        elif index == 95:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=85, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=88, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=88, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)       
        #Plan Pattern
        elif index == 96:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=90, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=92, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=92, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=4, interval=0.07)
        #Plan Calendar
        elif index == 97:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=93, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=98, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=95, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)  
        #Budget Volume
        elif index == 98:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=96, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=98, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=98, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)  
        #Plan Volume
        elif index == 99:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=99, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=101, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=101, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)  
        #Actual Volume
        elif index == 100:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=102, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=104, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=104, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)         
        #Actual Calendar
        elif index == 101:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=105, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=107, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=107, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)      
        #Generate Workload
        elif index == 102:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=109, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Lock Volume
        elif index == 103:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=111, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Run Priority Scheduling Engine
        elif index == 65:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=113, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Run Schedule Engine
        elif index == 104:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=117, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=4, interval=0.07)
                pass  #Regular
        #Schedule Day Lock
        elif index == 105:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=122, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=5, interval=0.07)
                pass  #Regular 
        #Shift Profile Sets
        elif index == 106:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=123, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=127, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=127, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)
        #Shift Profiles
        elif index == 107:
            if setting == 'EDIT & VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=128, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=132, interval=0.07)
                pass
            elif setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=132, interval=0.07)
                pass  #Regular   
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=4, interval=0.07)
            #4 Tabs to Enter Time Off     
        #Enter Time Off
        elif index == 108:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=138, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=6, interval=0.07)
                pass  #Regular
            #6 Tabs to Pay Code Edits using Pattern Day
        #Pay Code Edits using Pattern Day
        elif index == 109:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=146, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=8, interval=0.07)
                pass  #Regular
            #8 Tabs to Add to schedule Group 
        #Add to Schedule Group
        elif index == 110:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=148, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Remove from Schedule Group
        elif index == 111:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=150, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular    
        #Edit Group Schedules
        elif index == 112:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=152, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular    
        #Lock Shifts
        elif index == 113:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=154, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular     
        #Assign Breaks
        elif index == 114:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=156, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular 
        #Team Definition Setup
        elif index == 115:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=158, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular 
        #Team Definition Setup Extended Access
        elif index == 116:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=162, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular 
        #Replace shift
        elif index == 117:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=164, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular     
        #Append shift
        elif index == 118:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=166, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Insert transfer <Two Tabs to Employee visibility period and enter> Not closing any Drops 
        elif index == 119:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=76, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=76, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
        #Employee Visibility Periods
        elif index == 120:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=136, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=139, interval=0.07)
                pass    #Open    
        #Request Submission Control
        elif index == 121:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=141, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Request Period Extended Access
        elif index == 122:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=143, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular    
        #Recurrent / Rolling periods
        elif index == 123:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=145, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Multi-Group options
        elif index == 124:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=147, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Employee Priority option
        elif index == 125:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=149, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Personal Hyperfinds for Employee Query
        elif index == 126:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=151, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Visibility Period Actions
        elif index == 127:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=153, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Call Log
        elif index == 128:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=155, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Call List
        elif index == 129:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=157, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Group Edit Results
        elif index == 130:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=159, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Calendar views for Managers <Closing Scheduling with initial click and 26 Tabs> 
        elif index == 131:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=26, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=26, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
        
        #---------------------------------------------------------
        # Timecard Editor for Managers 
        if  index == 132:
             tab_and_open(33)
             time.sleep(1)            
        # Timecard access
        elif  index == 133:    
            press_tab_and_decide(setting,36)       
        # Allow negatives in Timecard Editor
        elif  index == 134:
            press_tab_and_decide(setting,38)                
        # Approval in Timecard Editor 
        elif  index == 135:
            tab_and_open(40)
            time.sleep(1)       
        # Add
        elif  index == 136:
            press_tab_and_decide(setting,43)           
        # Remove
        elif  index == 137:
            press_tab_and_decide(setting,45)           
        # Remove All
        elif  index == 138:
            press_tab_and_decide(setting,47)  
        # Edit data after non account approval by self
        elif  index == 139:
            press_tab_and_decide(setting,49)   
        # Edit data after non account approval by others
        elif  index == 140:
            press_tab_and_decide(setting,51) 
            # End of Approval in Timecard Editor (close)
            tab_and_open(40)
            time.sleep(1)
        # Cancel meal deductions in Timecard Editor
        elif  index == 141:
            press_tab_and_decide(setting,43)            
        # Comments in Timecard Editor
        elif  index == 142:
            press_tab_and_decide(setting,45)
            press_tab_and_decide(setting,46)                      
        # Notes for Comments in Timecard Editor 
        elif  index == 143:
            tab_and_open(48)
            time.sleep(1)           
        # Add or Remove
        elif  index == 144:
            press_tab_and_decide(setting,51)       
        # Remove Notes added by Others
        elif  index == 145:
            press_tab_and_decide(setting,53)
            # end of Notes for Comments in Timecard Editor (close)
            tab_and_open(48)
            time.sleep(1)           
        # Hours Worked amount in Timecard Editor
        elif  index == 146:
            press_tab_and_decide(setting,51)            
        # Pay codes in Timecard Editor 
        elif  index == 147:    
            tab_and_open(53)
            time.sleep(1)    
        # Edit
        elif  index == 148:
            press_tab_and_decide(setting,56)
        # View
        elif  index == 149:
            press_tab_and_decide(setting,58)
        # Move Amount
        elif  index == 150:
            press_tab_and_decide(setting,60)
        # Start Time on pay code edits
        elif  index == 151:
            press_tab_and_decide(setting,64)
        # Justify Missed Time Exceptions
        elif  index == 152:
            press_tab_and_decide(setting,66)
        # Mark Exceptions Reviewed in Timecard Editor
        elif  index == 153:
            press_tab_and_decide(setting,68)
            # End of Pay codes in Timecard Editor (close)
            tab_and_open(53)
            time.sleep(1)   
        # Punch edits in Timecard Editor
        elif  index == 154:
            press_tab_and_decide(setting,56)
        # Sign-off in Timecard Editor 
        elif  index == 155:    
            tab_and_open(58)
            time.sleep(1)
        # Add
        elif  index == 156:
            press_tab_and_decide(setting,61)
        # Remove
        elif  index == 157:
            press_tab_and_decide(setting,63)
            # End of Sign-off in Timecard Editor (close)
            tab_and_open(58)
            time.sleep(1)    
        # Calculate totals in Timecard Editor
        elif  index == 158:
            press_tab_and_decide(setting,61)
        # Totals breakdown in Timecard Editor
        elif  index == 159:
            press_tab_and_decide(setting,63)
        # Transfers in Timecard Editor 
        elif  index == 160:    
            tab_and_open(67)
            time.sleep(1)
        # View transfers
        elif  index == 161:
            press_tab_and_decide(setting,70)
        # Perform cost center transfers
        elif  index == 162:
            press_tab_and_decide(setting,72)
        # Perform labor category transfers
        elif  index == 163:
            press_tab_and_decide(setting,74)
        # Perform work rule transfers
        elif  index == 164:
            press_tab_and_decide(setting,76)
        # Perform job transfers
        elif  index == 165:
            press_tab_and_decide(setting,78)
            # End of Transfers in Timecard Editor (close)
            tab_and_open(67)
            time.sleep(1)      
        # View schedules in Timecard Editor
        elif  index == 166:
            press_tab_and_decide(setting,70)    
       # Accruals in Timecard Editor 
        elif  index == 167:    
           tab_and_open(74)
           time.sleep(1)       
       # Reports in Timecard Editor 
        elif  index == 168:    
            tab_and_open(79)
            time.sleep(1)
            # Sleeping for testing
            time.sleep(10)          
        # Rule Analysis Tool Report in Timecard editor
        elif  index == 169:
            press_tab_and_decide(setting,82)
            # End of Reports in Timecard Editor (close)
            tab_and_open(79)
            time.sleep(1)       
        # View the Audit Trail Tab in Timecard Editor
        elif  index == 170:
            press_tab_and_decide(setting,82)     
        # Enable Job Transfer Validation
        elif  index == 171:
            press_tab_and_decide(setting,86)
            # End of Timecard Editor for Managers (close)
            tab_and_open(33)
            time.sleep(1)
        # Multiple Assignments (Skip)
        # Activities in Timecard Editor (Skip)
        # Notes For Comments in Activities (Skip)
        # Accept Activities in Timecard Editor (Skip)
        
        # Reports 
        elif  index == 172:    
            tab_and_open(42)
            time.sleep(1)
        # Run reports
        elif  index == 173:
            press_tab_and_decide(setting,45)
        # Report scheduling
        elif  index == 174:
            press_tab_and_decide(setting,47)
        # Report setup (skip)
        # Schedule reports for others
        elif  index == 175:
            press_tab_and_decide(setting,52)
        # Report Scheduling: All Access
        elif  index == 176:
            press_tab_and_decide(setting,54)
        # Report Page
        elif  index == 177:
            press_tab_and_decide(setting,56)
        # Schedule report delivery to email as attachment
        elif  index == 178:
            press_tab_and_decide(setting,58)
            # Reports (close) 
            tab_and_open(42)
            time.sleep(1)
        # E-mail Notifications to Managers 
        elif  index == 179:    
            tab_and_open(45)
            time.sleep(1)
        # E-mail a completed group edit
        elif  index == 180:
            press_tab_and_decide(setting,48)
        # E-mail when a group edit was not completed
        elif  index == 181:
            press_tab_and_decide(setting,50)
        # E-mail when event status has changed
        elif  index == 182:
            press_tab_and_decide(setting,52)
            # E-mail Notifications to Managers (close)
            tab_and_open(45)
            time.sleep(1)
        # Manager access to Actions list
        elif  index == 183:
            press_tab_and_decide(setting,50)
        # Forecasting (skip)
        # Forecast Planner (skip)
        # Operational Dashboard (skip)
        
        # Attendance for Managers 
        elif  index == 184:    
            tab_and_open(55)
            time.sleep(1)
        # View Audit Data
        elif  index == 185:
            press_tab_and_decide(setting,58)
        # Perfect attendance definitions
        elif  index == 186:
            press_tab_and_decide(setting,60)
        # Source policy
        elif  index == 187:
            press_tab_and_decide(setting,62)
        # Attendance Actions
        elif  index == 188:
            tabto(64)
            if setting == 'All' or setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
        # Apply Rules
        elif  index == 189:
            tabto(66)
            if setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
        # Attendance Balance Resets and Adjustments
        elif  index == 190:
            # two fields that change together
            # Change field one
            tabto(68)
            if setting == 'All' or setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
            # Change field two    
            tabto(69)
            if setting == 'All' or setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
        # Attendance Events
        elif  index == 191:
            # three fields that change together
            # Change field one
            tabto(71)
            if setting == 'All' or setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
            # Change field two    
            tabto(72)
            if setting == 'All' or setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
            # Change field three    
            tabto(73)
            if setting == 'All' or setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
        # Refine Filters (skip)
        # Access to Attendance Detail Page and Calendar
        elif  index == 59:
            press_tab_and_decide(setting,80)       
        elif  index == 192:
            press_tab_and_decide(setting,80)
        # Forward Attendance Documents
        elif  index == 193:
            press_tab_and_decide(setting,82)
        # View Attendance Documents
        elif  index == 194:
            press_tab_and_decide(setting,84)
            # End of Attendance for Managers (close)
            tab_and_open(55)
            time.sleep(1)
        # Location Data 
        elif  index == 195:    
            tab_and_open(58)
            time.sleep(1)
        # View location data
        elif  index == 196:
            press_tab_and_decide(setting,61)
            # Location Data (close)
            tab_and_open(58)
            time.sleep(1)
        # Leave Cases For Managers 
        elif  index == 197:    
            tab_and_open(61)
            time.sleep(1)
        # Access to Leave Landing Page
        elif  index == 198:
            press_tab_and_decide(setting,64)
        # Access to Leave Case Editor, Leave Calendar and Takings List
        elif  index == 199:
            press_tab_and_decide(setting,66)
        # Access to Leave Audit
        elif  index == 200:
            press_tab_and_decide(setting,68)
        # Manage Leave Case 
        elif  index == 201:    
            tab_and_open(70)
            time.sleep(1)
        # Leave Case Details (skip)
        # Leave Case Eligibility and Rules (skip)        
        # Leave Case Documents 
        elif  index == 202:    
            tab_and_open(85)
            time.sleep(1) 
        # Forward documents
        elif  index == 203:
            tabto(88)
            if setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)        
        # View documents
        elif  index == 204:
            tabto(92)
            if setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
            # End of Leave Case Documents (close)
            tab_and_open(85)
            time.sleep(1)
        # Leave Case Additional Information
        elif  index == 205:
            tabto(88)
            if setting == 'allowed':
                pyautogui.press('a')
                time.sleep(2)
            elif setting == 'All But Self':
                pyautogui.press('up')
                time.sleep(2)
        # Leave Case Notes
        elif  index == 206:
            if setting == 'VIEW-Allowed':
                tabto(93)
                pyautogui.press('a')
                time.sleep(2)
            # Manage Leave Case (close)
            tab_and_open(70)
            time.sleep(1)
            # Leave Cases For Managers (close)
            tab_and_open(61)
            time.sleep(1)
            
        # Leave Case Notifications (skip)
        # Leave of Absence Time (skip)
        # Leave time in Timecard Editor (skip)
        # Leave time in Scheduling (skip)
        # Leave time actions (skip)
        # Commit to Timecard (skip)
        # Commit to Schedule (skip)
        
        # Edit signed off time 
        elif  index == 207:    
            tab_and_open(66)
            time.sleep(1)
        # Allow enable edits for employees
        elif  index == 208:
            press_tab_and_decide(setting,73)
            # End of Edit signed off time (close)
            tab_and_open(66)
            time.sleep(1) 
        # Dataview Personalization
        elif  index == 209:
            press_tab_and_decide(setting,69)
        # Include inactive and terminated employees into search result
        elif  index == 210:
            press_tab_and_decide(setting,71)
        #Employee Search
        elif  index == 211:
            press_tab_and_decide(setting,73)
            # End of dept Manager (close)
            tab_and_open(20)
            time.sleep(1)    
        #----------------------------------#    
        #Manager - Common Setup
        elif index == 212:
            if setting == '' or setting == 'None':                
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=23, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=24, interval=0.07)
                pyautogui.press('up')  # Assuming <up> to disallow
                pass
        #Hyperfind
        elif index == 213:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=26, interval=0.07)
                pyautogui.press('enter')
                pass
        #Query conditions
        elif index == 214:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=29, interval=0.07)
                pyautogui.press('enter')        
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=32, interval=0.07)
                pyautogui.press('up')  # Assuming <up> to disallow
                pass
        #Display Business Structure & Job Information in Hyperfind
        elif index == 215:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=34, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #General Information category
        elif index == 216:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=36, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Timekeeper category
        elif index == 217:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=38, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Time Management category
        elif index == 218:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=42, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Scheduler category
        elif index == 219:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=44, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Advanced Scheduler category
        elif index == 220:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=50, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #User Information category
        elif index == 221:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=52, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Role - Timekeeper category
        elif index == 222:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=60, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Attendance Category
        elif index == 223:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=29, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=29, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
        #Query tabs
        elif index == 224:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=32, interval=0.07)
                pyautogui.press('enter')        
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=35, interval=0.07)
                pyautogui.press('up')  # Assuming <up> to disallow
                pass
        #Assemble Query tab
        elif index == 225:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=32, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=32, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
        #Query visibility
        elif index == 226:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=35, interval=0.07)
                pyautogui.press('enter')        
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=38, interval=0.07)
                pyautogui.press('up')  # Assuming <up> to disallow
                pass
        #Ad hoc queries
        elif index == 227:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=40, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Personal queries
        elif index == 228:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=41, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position
                pyautogui.press('tab', presses=46, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=6, interval=0.07)
                pass  #Regular
        #Query Manager
        elif index == 229:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=26, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=26, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
        #People Editor
        elif index == 230:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=29, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=32, interval=0.07)
                pass    #Open    
        #Person
        elif index == 231:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=33, interval=0.07)
                pyautogui.write('All')
                pyautogui.press('tab', presses=38, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=6, interval=0.07)
                pass  #Regular    
        #License view
        elif index == 232:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=39, interval=0.07)
                pyautogui.press('up')
                pyautogui.press('tab', presses=41, interval=0.07)
                pass
            elif setting == 'disallowed':
                pass  #Regular       
#---------------------------------------------------------------------------------#
#Employee Group
        elif index == 233:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=41, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pass    #Open
        #Information view
        elif index == 234:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=44, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=50, interval=0.07)
                pass    #Open
        #Person name
        elif index == 235:
            if setting == 'VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=52, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular    
        #Person ID
        elif index == 236:
            if setting == 'VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=54, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Hire date
        elif index == 237:
            if setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=57, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular
        #Employment status
        elif index == 238:
            if setting == 'VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=62, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=5, interval=0.07)
                pass  #Regular
        #Access user account
        elif index == 239:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=62, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=65, interval=0.07)
                pass    #Open
        #User name
        elif index == 240:
            if setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=81, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=16, interval=0.07)
                pass  #Regular
        #Primary Labor Category
        elif index == 241:
            if setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=84, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)
                pass  #Regular
        #Primary Job
        elif index == 242:
            if setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=87, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)
                pass  #Regular
        #Time Zone  
        elif index == 243:
            if setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=62, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=62, interval=0.07)
                pyautogui.press('enter')
                pass  #Regular
        #Reports To
        elif index == 244:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=76, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=79, interval=0.07)
                pass    #Open
        #Reports To Field
        elif index == 245:
            if setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=82, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=3, interval=0.07)
                pyautogui.press('enter')
                pass  #Regular
        #Manager ID Column
        elif index == 246:
            if setting == 'VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=84, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=2, interval=0.07)
                pass  #Regular    
        #Seniority Date
        elif index == 247:
            if setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=44, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=44, interval=0.07)
                pyautogui.press('enter')
                pass  #Regular
        #Contact Information view
        elif index == 248:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=47, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=53, interval=0.07)
                pass    #Open
        #E-mail
        elif index == 249:
            if setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=56, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)
                pass  #Regular 
        #Telephone
        elif index == 250:
            if setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=62, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=6, interval=0.07)
                pass  #Regular 
        #Additional Information view
        elif index == 251:
            if setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=65, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=3, interval=0.07)
                pass  #Regular 
        #Person's Dates View
        elif index == 252:
            if setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=41, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=41, interval=0.07)
                pyautogui.press('enter')
                pass  #Closes Contact information view dropdown 
        # Timekeeping Group
        elif index == 253:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=47, interval=0.07)
                pyautogui.press('enter')
                pass    #Open    
        #Timekeeper view
        elif index == 254:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=53, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=56, interval=0.07)
                pass    #Open
        #Percent Allocation Assignment
        elif index == 255:
            if setting == 'VIEW-Allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=68, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=12, interval=0.07)
                pass  #Regular    
        #Employment Terms view
        elif index == 256:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=47, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=47, interval=0.07)
                pyautogui.press('enter')
                pass    #Close
        #Scheduling Group
        elif index == 257:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=50, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=53, interval=0.07)
                pass    #Open
        #Scheduler view
        elif index == 258:
            if setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=1, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=6, interval=0.07)
                pass  #Regular
        #Skills & Certifications view
        elif index == 259:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=59, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=62, interval=0.07)
                pass    #Open
        #Skills on a person
        elif index == 260:
            if setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=3, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=67, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=5, interval=0.07)
                pass  #Regular
        #Certifications on a person
        elif index == 261:
            if setting == 'allowed':
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position
                pyautogui.press('tab', presses=68, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position
                pyautogui.press('tab', presses=69, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=70, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=29, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=29, interval=0.07)
                pyautogui.press('enter')
                pass  #Close
        #Event Manager
        elif index == 262:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=45, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=52, interval=0.07)
                pass    #Open
        #Individual events
        elif index == 263:   
            if setting == 'ONLY SELF':
                pyautogui.press('O')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=45, interval=0.07)
                pyautogui.press('enter')

                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y) 
                pyautogui.press('tab', presses=45, interval=0.07)
                pyautogui.press('enter')
                pass    #Close       
        #Schedule Configuration
        elif index == 264:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=58, interval=0.07)
                pyautogui.press('enter')
                pass    #Open
        #Skills & Certifications
        elif index == 265:
            if setting == '':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=66, interval=0.07)
                pyautogui.press('enter')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=69, interval=0.07)
                pass    #Open
        #Certifications
        elif index == 266:
            if setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=3, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=74, interval=0.07)
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=5, interval=0.07)
                pass  #Regular
        #Skills
        elif index == 267:
            if setting == 'VIEW-Allowed':
                pyautogui.press('tab', presses=3, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=66, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=66, interval=0.07)
                pyautogui.press('enter')
                pass  #Regular
        #Shift Template Configuration
        elif index == 268:
            if setting == 'EDIT & VIEW-Allowed':
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=84, interval=0.07)
                pyautogui.press('up')
                mouse_click(initial_x, initial_y)  # Reset click position 
                #
                #
                #Quuestioni in Regards to the schedule template config only Edit option no view (Program works by- enabling only the edit and disallowing the add and delete options)
                #pyautogui.press('tab', presses=86, interval=0.07)
                #pyautogui.press('up')
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=23, interval=0.07)
                pyautogui.press('enter')
                pass
            elif setting == 'disallowed':
                mouse_click(initial_x, initial_y)
                pyautogui.press('tab', presses=23, interval=0.07)
                pyautogui.press('enter')
                pass  #Regular
        #Manager - System Configuration
        elif index == 269:
            if setting == 'allowed':
                mouse_click(initial_x, initial_y)  # Reset click position 
                pyautogui.press('tab', presses=27, interval=0.07)
                pyautogui.press('up')
                pass
            elif setting == 'disallowed':
                pyautogui.press('tab', presses=27, interval=0.07)
                pyautogui.press('down')
                pass  #Regular
        
        
        '''
        End Of Program
        Manager System Config Disallow All. 
        All thanks to Kevin and Timi. 
        '''
        
        # Delay to avoid sending inputs too quickly
        time.sleep(0.5)





#The Kwiggler Script Functions for safety-------------------------------------------------------------------------------------------------------------------
#Functions 
def move_and_click(x, y, delay=0.7):
    """
    Moves the mouse to a specified position and clicks.
    Parameters:
    - x (int): The x-coordinate to move the mouse to.
    - y (int): The y-coordinate to move the mouse to.
    - delay (float): The time in seconds to wait after the click. Default is 0.7 seconds.
    """
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(delay)
    
def mouse_click(x, y):
    pyautogui.click(x, y)    

def tabto(count,initial_x=1291, initial_y=100):
    mouse_click(initial_x, initial_y)
    pyautogui.press('tab', presses=count, interval=0.07)
                
# Function to press tab the required number of times and then either up+tab or down based on the setting
def press_tab_and_decide(setting, tabs_count):
    print(f"{setting}: ")
    # Press tab the required number of times
    tabto(tabs_count)
    # Decide whether to press 'up' and 'tab' or just 'down'
    if setting == 'allowed' or setting == "All But Self":
        pyautogui.press('up')
        
        time.sleep(2)
    #elif setting == 'All':
    #    pyautogui.press('a')
    #    time.sleep(2)
    else:
        pyautogui.press('down')
    time.sleep(0.7)

def tab_and_open(count):
    print(f"expand")
    tabto(count)
    pyautogui.press('enter')
    time.sleep(1)
#End of The Kwiggler's Functions -------------------------------------------------------------------------------------------------------------------

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
