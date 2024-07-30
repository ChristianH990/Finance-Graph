#Time

import time


#Start UI
def message(string):  
    for i in string:      
        print(i, end="")             
        time.sleep(0.008)
if __name__ == '__main__':
    msg = "--------------------------------\n----- FINANCIAL VISUALIZER -----\n--------------------------------"
    message(msg)


def message(string):  
    for i in string:      
        print(i, end="")             
        time.sleep(0.1)
if __name__ == '__main__':
    msg = "\n\n©Copyright Hillier Technologies\nJuly 2024"
    message(msg)
print()
print()
time.sleep(0.5)
def message(string):  
    for i in string:      
        print(i, end="")             
        time.sleep(0.1)
if __name__ == '__main__':
    msg = "DevBuild 1.3.3"
    message(msg)
print('\n')
time.sleep(2)


# Inputs

repeat_count_begining = 1
while repeat_count_begining <= 10:
    def message(string):  
        for i in string:      
            print(i, end="")             
            time.sleep(0.016)
    if __name__ == '__main__':
        msg = "\nAnnual Salary($)"
        message(msg)
    variable1_input = input(':\n')


    #DEBUG

    if variable1_input == '88224646':
        print()
        print()
        print()
        def message(string):  
            for i in string:      
                print(i, end="")             
                time.sleep(0.05)
        if __name__ == '__main__':
            msg = "A FATAL ERROR HAS OCCURED!" 
            message(msg)
        time.sleep(1)
        def message(string):  
            for i in string:      
                print(i, end="")             
                time.sleep(0.05)
        if __name__ == '__main__':
            msg = "\nRebooting" 
            message(msg)
        time.sleep(0.7)
        def message(string):  
            for i in string:      
                print(i, end="")             
                time.sleep(0.7)
        if __name__ == '__main__':
            msg = "..." 
            message(msg)


        #DEBUG UI 
        debug_ui_loop = 1
        while debug_ui_loop <= 10:
            debug_ui_loop += 1
            print()
        def message(string):  
            for i in string:      
                print(i, end="")             
                time.sleep(0.006)
        if __name__ == '__main__':
            msg = "\n--------------------------------  ▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░\n----- FINANCIAL VISUALIZER -----  ▐▓█░░░░░░░░░█▓▌░█▄▄▄█░\n--------------------------------  ▐▓█░░░░░░░░░█▓▌░█▄▄▄█░\n      DEBUG MODE                  ▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░\n                                  ░░░░░░███░░░░░░░█▄▄▄█░\n                                  ░░░░▄▄███▄▄░░░░░█████░"
            message(msg)


        def message(string):  
            for i in string:      
                print(i, end="")             
                time.sleep(0.1)
        if __name__ == '__main__':
            msg = "\n\n©Copyright Hillier Technologies\nJuly 2024"
            message(msg)
        print()
        print()
        print()
        

        data_loop = 1
        while data_loop <=10:
            time.sleep(2)
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.016)
            if __name__ == '__main__':
                msg = "Valid, Invalid, or Negative data?(V,I or N)"
                message(msg)
            debugdata = input(':\n').lower()

            if debugdata == 'v':
                def message(string):  
                    for i in string:      
                        print(i, end="")             
                        time.sleep(0.016)
                if __name__ == '__main__':
                    msg = "\n\nValid data choosen."
                    message(msg)
                variable1_input = '30000'
                variable2_input = '500'
                variable3_input = '100'
                variable4_input = '100'
                variable5_input = '1000'
                data_loop +=11
            
            elif debugdata == 'i':
                def message(string):  
                    for i in string:      
                        print(i, end="")             
                        time.sleep(0.016)
                if __name__ == '__main__':
                    msg = "\n\nInvalid data choosen."
                    message(msg)
                variable1_input = '10000'
                variable2_input = 'wsasd'
                variable3_input = '100'
                variable4_input = '100'
                variable5_input = '1000'
                data_loop +=11
            
            elif debugdata == 'n':
                def message(string):  
                    for i in string:      
                        print(i, end="")             
                        time.sleep(0.016)
                if __name__ == '__main__':
                    msg = "\n\nNegative data choosen."
                    message(msg)
                variable1_input = '10000'
                variable2_input = '500'
                variable3_input = '100'
                variable4_input = '100'
                variable5_input = '1000'
                data_loop +=11
            else:
                print()
                print()
                def message(string):  
                    for i in string:      
                        print(i, end="")             
                        time.sleep(0.016)
                if __name__ == '__main__':
                    msg = "\nInvalid response, please try again"
                    message(msg)
                data_loop += 0
            #DEBUG NumericalCheck

        def isinvalid(variable1_input):
            for variable1_input in variable1_input:
                if variable1_input.isnumeric() == False and variable1_input != '.':
                    return True
            return False
            
        if isinvalid(variable1_input):
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nSalary has an INVALID input."
                message(msg)   
        else:
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nSalary has a VALID input."
                message(msg)   

        def isinvalid(variable2_input):
            for variable2_input in variable2_input:
                if variable2_input.isnumeric() == False and variable2_input != '.':
                    return True
            return False    
        if isinvalid(variable2_input):
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nHousing has an INVALID input."
                message(msg)   
        else:
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nHousing has a VALID input."
                message(msg)   

        def isinvalid(variable3_input):
            for variable3_input in variable3_input:
                if variable3_input.isnumeric() == False and variable3_input != '.':
                    return True
            return False    
        if isinvalid(variable3_input):
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nBills has an INVALID input."
                message(msg)   
        else:
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nBills has a VALID input."
                message(msg)   

        def isinvalid(variable4_input):
            for variable4_input in variable4_input:
                if variable4_input.isnumeric() == False and variable4_input != '.':
                    return True
            return False    
        if isinvalid(variable4_input):
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nFood has an INVALID input."
                message(msg)   
        else:
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nFood has a VALID input."
                message(msg)   

        def isinvalid(variable5_input):
            for variable5_input in variable5_input:
                if variable5_input.isnumeric() == False and variable5_input != '.':
                    return True
            return False    
        if isinvalid(variable5_input):
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nTravel has an INVALID input."
                message(msg)   
        else:
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nTravel has a VALID input."
                message(msg)   
        if isinvalid(variable1_input) or isinvalid(variable2_input) or isinvalid(variable3_input) or isinvalid(variable4_input) or isinvalid(variable5_input):
            print('\nOne or more Inputs is invalid, please try again.')
            time.sleep(1.5)
            repeat_count_begining += 0
        else:    
            repeat_count_begining += 11
            print()
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nBuilding Graph"
                message(msg)  
            time.sleep(0.3)
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.3)
            if __name__ == '__main__':
                msg = "..." 
                message(msg)
            time.sleep(0.3)
            
            print_graph_loop = 1
            while print_graph_loop < 6:
                print()
                print_graph_loop += 1

            # DEBUG Calculations
            variable1_input = float(variable1_input) #Annual Income
            variable2_input = float(variable2_input) #Monthly Housing
            variable3_input = float(variable3_input) #Monthly Bills
            variable4_input = float(variable4_input) #Weekly Food
            variable5_input = float(variable5_input) #Annual Travel

            annual_housing = variable2_input * 12
            annual_bills = variable3_input * 12
            annual_food = variable4_input * 52


            #DEBUG Taxes

            alberta_tax = 0.05
            taxes = variable1_input * alberta_tax

            extra = variable1_input - (annual_housing + annual_bills + annual_food + variable5_input + taxes)


            #DEBUG Graph
           
            extra_percentage =   extra / variable1_input* 100
            taxes_percentage = taxes / extra * 100 
            housing_percentage =  annual_housing / extra * 100 
            bills_percentage = annual_bills / extra * 100 
            annual_food_percentage = annual_food / extra * 100 
            travel_percentage = variable5_input / extra * 100 

            housing_amountgraph = 'housing | $' + format(annual_housing, '11,.2f') + ' '
            housing_percentgraph = '| ' + format(housing_percentage, '5,.1f') + '% | ' + ('#' * int(housing_percentage))
            housing_graph =  housing_amountgraph + housing_percentgraph

            bills_amountgraph = '  bills | $' + format(annual_bills, '11,.2f') + ' '
            bills_percentgraph = '| ' + format(bills_percentage, '5,.1f') + '% | ' + ('#' * int(bills_percentage))
            bills_graph = bills_amountgraph + bills_percentgraph
            
            food_amountgraph = '   food | $' + format(annual_food, '11,.2f') + ' '
            food_percentgraph = '| ' + format(annual_food_percentage, '5,.1f') + '% | ' + ('#' * int(annual_food_percentage))
            food_graph =  food_amountgraph + food_percentgraph
            
            travel_amountgraph = ' travel | $' + format(variable5_input, '11,.2f') + ' '
            travel_percentgraph = '| ' + format(travel_percentage, '5,.1f') + '% | ' + ('#' * int(travel_percentage))
            travel_graph = travel_amountgraph + travel_percentgraph

            tax_amountgraph = '    tax | $' + format(taxes, '11,.2f') + ' '
            tax_percentgraph = '| ' + format(taxes_percentage, '5,.1f') + '% | ' + ('#' * int(taxes_percentage))
            tax_graph =  tax_amountgraph + tax_percentgraph

            extra_amountgraph = '  extra | $' + format(extra, '11,.2f') + ' '
            extra_percentgraph = '| ' + format(extra_percentage, '5,.1f') + '% | ' + ('#' * int(extra_percentage))
            extra_graph =  extra_amountgraph + extra_percentgraph
            
        
            #DEBUG Graph UI            
            
            width = int(max(taxes_percentage, housing_percentage, bills_percentage, annual_food_percentage, travel_percentage, extra_percentage))
            boundaryequation = (34 + width)
            boundary = '-' * boundaryequation
            text_boundaryequationp1 = (boundaryequation / 2) - 7
            text_boundaryequationp2 = int(text_boundaryequationp1) * '-' 
            spaceboundary = ('                           ')
            print()
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (spaceboundary + 'EXPENSES CHART\n')
                message(msg)      
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (boundary + '\n')
                message(msg)   
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (housing_graph + '\n')
                message(msg)  
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (bills_graph + '\n')
                message(msg)
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (food_graph + '\n')
                message(msg)
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (travel_graph + '\n')
                message(msg)
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (tax_graph + '\n')
                message(msg)
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (extra_graph + '\n')
                message(msg)
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (boundary + '\n')
                message(msg) 
            print()
            print()
            print()
            
            if extra < int(0):
                def message(string):  
                    for i in string:      
                        print(i, end="")             
                        time.sleep(0.011)
                if __name__ == '__main__':
                    msg = ('UH OH, your extra money is in the negatives!')
                    message(msg) 
                time.sleep(0.5)
                def message(string):  
                    for i in string:      
                        print(i, end="")             
                        time.sleep(0.011)
                if __name__ == '__main__':
                    msg = ('\nYou should consider changing your spending habits.\n')
                    message(msg)
            #Exit Loop


            time.sleep(5)
            exit_loop = 0
            while exit_loop <= 3:   
                def message(string):  
                    for i in string:      
                            print(i, end="")             
                            time.sleep(0.016)
                if __name__ == '__main__':
                    msg = "Exit Program? Y or N"
                    message(msg)
                end = input('\n').lower()
                if end == 'y':
                    def message(string):  
                        for i in string:      
                            print(i, end="")             
                            time.sleep(0.016)
                    if __name__ == '__main__':
                        msg = "\nExiting Program"
                        message(msg)
                        time.sleep(0.7)
                        def message(string):  
                            for i in string:      
                                print(i, end="")             
                                time.sleep(0.7)
                        if __name__ == '__main__':
                            msg = "..." 
                            message(msg)
                        exit_loop += 4
                elif end == 'n':
                        exit_loop +=4
                        repeat_count_begining -=10
                        repeat_count_begining += 0
                else: 
                    def message(string):  
                        for i in string:      
                            print(i, end="")             
                            time.sleep(0.016)
                    if __name__ == '__main__':
                        msg = "\nUnknown response, please try again\n."
                        message(msg)
                        time.sleep(1.5)
                        exit_loop += 0


        #Main Script

    else:
        def message(string):  
            for i in string:      
                print(i, end="")             
                time.sleep(0.016)
        if __name__ == '__main__':
            msg = "\nMonthly Housing Costs($)"
            message(msg)
        variable2_input = input(':\n')

        def message(string):  
            for i in string:      
                print(i, end="")             
                time.sleep(0.016)
        if __name__ == '__main__':
            msg = "\nMonthly Bill Costs($)"
            message(msg)
        variable3_input = input(':\n')

        def message(string):  
            for i in string:      
                print(i, end="")             
                time.sleep(0.016)
        if __name__ == '__main__':
            msg = "\nWeekly Food Costs($)"
            message(msg)
        variable4_input = input(':\n')

        def message(string):  
            for i in string:      
                print(i, end="")             
                time.sleep(0.016)
        if __name__ == '__main__':
            msg = "\nAnnual Travel Costs($)"
            message(msg)
        variable5_input = input(':\n')


        #NumericalCheck

        def isinvalid(variable1_input):
            for variable1_input in variable1_input:
                if variable1_input.isnumeric() == False and variable2_input != '.':
                    return True
            return False
        time.sleep(0.25)
        if isinvalid(variable1_input):
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nSalary has an INVALID input."
                message(msg)   
        else:
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nSalary has a VALID input."
                message(msg)   

        def isinvalid(variable2_input):
            for variable2_input in variable2_input:
                if variable2_input.isnumeric() == False and variable2_input != '.':
                    return True
            return False    
        time.sleep(0.25)
        if isinvalid(variable2_input):
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nHousing has an INVALID input."
                message(msg)   
        else:
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nHousing has a VALID input."
                message(msg)   
        def isinvalid(variable3_input):
            for variable3_input in variable3_input:
                if variable3_input.isnumeric() == False and variable3_input != '.':
                    return True
            return False    
        time.sleep(0.25)
        if isinvalid(variable3_input):
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nBills has an INVALID input."
                message(msg)   
        else:
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nBills has a VALID input."
                message(msg)   

        def isinvalid(variable4_input):
            for variable4_input in variable4_input:
                if variable4_input.isnumeric() == False and variable4_input != '.':
                    return True
            return False  
        time.sleep(0.25)  
        if isinvalid(variable4_input):
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nFood has an INVALID input."
                message(msg)   
        else:
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nFood has a VALID input."
                message(msg)   

        def isinvalid(variable5_input):
            for variable5_input in variable5_input:
                if variable5_input.isnumeric() == False and variable5_input != '.':
                    return True
            return False    
        
        time.sleep(0.25)
        
        if isinvalid(variable5_input):
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nTravel has an INVALID input."
                message(msg)   
        else:
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nTravel has a VALID input."
                message(msg)   
        
        time.sleep(0.5)

        if isinvalid(variable1_input) or isinvalid(variable2_input) or isinvalid(variable3_input) or isinvalid(variable4_input) or isinvalid(variable5_input):
            print('\nOne or more Inputs is invalid, please try again.')
            time.sleep(1.5)
            repeat_count_begining += 0
        else:    
            repeat_count_begining += 11
            print()
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.008)
            if __name__ == '__main__':
                msg = "\nBuilding Graph"
                message(msg)  
            time.sleep(0.3)
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.3)
            if __name__ == '__main__':
                msg = "..." 
                message(msg)
            time.sleep(0.3)
            
            print_graph_loop = 1
            while print_graph_loop < 6:
                print()
                print_graph_loop += 1

            #Calculations
            variable1_input = float(variable1_input) #Annual Income
            variable2_input = float(variable2_input) #Monthly Housing
            variable3_input = float(variable3_input) #Monthly Bills
            variable4_input = float(variable4_input) #Weekly Food
            variable5_input = float(variable5_input) #Annual Travel

            annual_housing = variable2_input * 12
            annual_bills = variable3_input * 12
            annual_food = variable4_input * 52


            #Taxes

            alberta_tax = 0.95
            alberta_tax2 = 0.05
            taxes = variable1_input * alberta_tax2

            extra = variable1_input - (annual_housing + annual_bills + annual_food + variable5_input + taxes)


            #Graph

            extra_percentage =   extra / variable1_input* 100
            taxes_percentage = taxes / extra * 100 
            housing_percentage =  annual_housing / extra * 100 
            bills_percentage = annual_bills / extra * 100 
            annual_food_percentage = annual_food / extra * 100 
            travel_percentage = variable5_input / extra * 100 

            housing_amountgraph = 'housing | $' + format(annual_housing, '11,.2f') + ' '
            housing_percentgraph = '| ' + format(housing_percentage, '5,.1f') + '% | ' + ('#' * int(housing_percentage))
            housing_graph =  housing_amountgraph + housing_percentgraph

            bills_amountgraph = '  bills | $' + format(annual_bills, '11,.2f') + ' '
            bills_percentgraph = '| ' + format(bills_percentage, '5,.1f') + '% | ' + ('#' * int(bills_percentage))
            bills_graph = bills_amountgraph + bills_percentgraph
            
            food_amountgraph = '   food | $' + format(annual_food, '11,.2f') + ' '
            food_percentgraph = '| ' + format(annual_food_percentage, '5,.1f') + '% | ' + ('#' * int(annual_food_percentage))
            food_graph =  food_amountgraph + food_percentgraph
            
            travel_amountgraph = ' travel | $' + format(variable5_input, '11,.2f') + ' '
            travel_percentgraph = '| ' + format(travel_percentage, '5,.1f') + '% | ' + ('#' * int(travel_percentage))
            travel_graph = travel_amountgraph + travel_percentgraph

            tax_amountgraph = '    tax | $' + format(taxes, '11,.2f') + ' '
            tax_percentgraph = '| ' + format(taxes_percentage, '5,.1f') + '% | ' + ('#' * int(taxes_percentage))
            tax_graph =  tax_amountgraph + tax_percentgraph

            extra_amountgraph = '  extra | $' + format(extra, '11,.2f') + ' '
            extra_percentgraph = '| ' + format(extra_percentage, '5,.1f') + '% | ' + ('#' * int(extra_percentage))
            extra_graph =  extra_amountgraph + extra_percentgraph
            
        
            #Graph UI            
            
            width = int(max(taxes_percentage, housing_percentage, bills_percentage, annual_food_percentage, travel_percentage, extra_percentage))
            boundaryequation = (34 + width)
            boundary = '-' * boundaryequation
            text_boundaryequationp1 = (boundaryequation / 2) - 7
            text_boundaryequationp2 = int(text_boundaryequationp1) * '-' 
            spaceboundary = ('                           ')
            print()
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (spaceboundary + 'EXPENSES CHART\n')
                message(msg)      
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (boundary + '\n')
                message(msg)   
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (housing_graph + '\n')
                message(msg)  
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (bills_graph + '\n')
                message(msg)
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (food_graph + '\n')
                message(msg)
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (travel_graph + '\n')
                message(msg)
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (tax_graph + '\n')
                message(msg)
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (extra_graph + '\n')
                message(msg)
            def message(string):  
                for i in string:      
                    print(i, end="")             
                    time.sleep(0.011)
            if __name__ == '__main__':
                msg = (boundary + '\n')
                message(msg) 
            print()
            print()
            print()
            if extra < int(0):
                def message(string):  
                    for i in string:      
                        print(i, end="")             
                        time.sleep(0.011)
                if __name__ == '__main__':
                    msg = ('UH OH, your extra money is in the negatives!')
                    message(msg) 
                time.sleep(0.5)
                def message(string):  
                    for i in string:      
                        print(i, end="")             
                        time.sleep(0.011)
                if __name__ == '__main__':
                    msg = ('\nYou should consider changing your spending habits.\n')
                    message(msg)
            
            
            #Exit Loop

            time.sleep(5)
            exit_loop = 0
            while exit_loop <= 3:   
                def message(string):  
                    for i in string:      
                        print(i, end="")             
                        time.sleep(0.016)
                if __name__ == '__main__':
                    msg = "Exit Program? Y or N"
                    message(msg)
                end = input('\n').lower()
                if end == 'y':
                    def message(string):  
                        for i in string:      
                            print(i, end="")             
                            time.sleep(0.016)
                    if __name__ == '__main__':
                        msg = "\nExiting Program"
                        message(msg)
                    time.sleep(0.7)
                    def message(string):  
                        for i in string:      
                            print(i, end="")             
                            time.sleep(0.7)
                    if __name__ == '__main__':
                        msg = "..." 
                        message(msg)
                    exit_loop += 4
                elif end == 'n':
                    exit_loop +=4
                    repeat_count_begining -=10
                    repeat_count_begining += 0
                else: 
                    def message(string):  
                        for i in string:      
                            print(i, end="")             
                            time.sleep(0.016)
                    if __name__ == '__main__':
                        msg = "\nUnknown response, please try again.\n"
                        message(msg)
                    time.sleep(1.5)
                    exit_loop += 0