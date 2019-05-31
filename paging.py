#Zuqhame Skosana
#SKSZUQ001
#Operating Systems assignment 1

import random
import sys


#FIFO Implementation, accepting 3 parameters, 
#first parameter is size_page_frame
#second parameter is the list or array that is used (The one with numbers from 0-9 generated randomly)
#third parameter is a int value which is the size of the arrayList (get from user)

#------------------------------------------------------------------FIRST IN FIRST OUT-------------------------------------------------------------------------

def first_in_first_out_(size_page_frame,arrList,val1):
     #iniitialize variables 
    
    _pgs_ , divisor , faulty_pages, x, v  = [] , -1, 0, 0, -1
    

    while(x<=size_page_frame):
		_pgs_.append(-1)
		x=x+1
		
  

    for x in range(val1):
        
        boolean=False
        
      
        for y in range(size_page_frame):
            if(_pgs_[y] is arrList[x]):
               
                boolean=True
                break
        
       
        if boolean is False:
            divisor=(divisor+1)%size_page_frame
            _pgs_[divisor] = arrList[x]
            
            faulty_pages=faulty_pages+1
            
            print "{:<5}".format((("\n%d -->>" % (arrList[x])))), 
            
            for y in range(size_page_frame):
                if _pgs_[y] is not v: # v=is initialized to negetive 1
                    print _pgs_[y],
                else:
                    print ("[*]"), # [] shows that still need to be filled
        else:
			
			print "\n%d -->> no fault" % (arrList[x]),
    v_fifo=faulty_pages        
    print ("\n\nFirst in First out had: %d page faults." % (faulty_pages)+"\n"),


#Least Recently Used Page Replacement Algorithm,
#3 parameters used
#first parameter is size_page_frame
#second parameter is the list or array that is used (The one with numbers from 0-9 generated randomly)
#third parameter is a int value which is the size of the arrayList, recieved from the user

#---------------------------------------------------------------LEAST RECENTLY USED-------------------------------------------------------------------------------
def least_recently_used(size_page_frame,arrList,val1):
	
    _pgs_ = []  
    num_decider=0
    faulty_pages=0
    x=0
    v=-1
    
    while(x<=size_page_frame):
		_pgs_.append(v)
		x=x+1
		
    for x in range(val1):
        boolean = False
        for y in range(size_page_frame):
            if(_pgs_[y] is arrList[x]):
                boolean = True
                break
                
            
        if boolean is False:
            if _pgs_[num_decider] is not v: #v=-1
				
                minimum_number = 999
                
                for xy in range(size_page_frame):
                    y =  x       
                    check = False

                    for c in range(y):
						y=y-1
						if(_pgs_[xy] is arrList[y]):
							check=True
							break

                    if (minimum_number > y and check is True):
                        num_decider = xy
                        minimum_number = y
                        

            _pgs_[num_decider] = arrList[x] 
            num2=(num_decider+1)
            
            num_decider= (num2) % (size_page_frame)
            
            faulty_pages=faulty_pages+1
            
            print "\n%d -->>" % (arrList[x]),
            
            for y in range(size_page_frame):
                if _pgs_[y] is v:
                    
                    print "[*]", # [] shows that still need to be filled
                else:
                    print _pgs_[y],
        else:
			
            print "\n%d ->no faults" % (arrList[x]),
    v_lru=faulty_pages        
    print "\n\nLeast recently used had : %d page faults." % (faulty_pages)


#Optimal Page Replacement Algorithm
#3 parameters used
#first parameter is size_page_frame
#second parameter is the list or array that is used (The one with numbers from 0-9)
#third parameter is a int value which is the size of the arrayList, this is recieved from user

#-----------------------------------------------------------------------------OPTIMAL PAGE REPLACEMENT-----------------------------------------------------------------------
def optimal_page_replacement(size_page_frame,arrList,val1):
    

    x, faulty_pages, _pgs_, val_Rands, v, w = 0, 0, [], -1, -1, 0  #initiaize local variables
    
    while(w<=size_page_frame):
		_pgs_.append(v)
		w=w+1
  
   
		
    for xx in range(val1):
        
        check = False
        yy=0
        
        while (yy <= size_page_frame):
			if(_pgs_[yy] is arrList[xx]):
				check=True
				break
			yy=yy+1


            
        if check is False:
      
        
            isFault, n_avail_s =False, val_Rands
            
            val3=0
            while(val3<=size_page_frame):
				if  _pgs_[val3] is val_Rands:
					isFault=True
					n_avail_s=val3
				val3+=1
            

            
            if not isFault:
                

                numm1 , numm2 = 0, val_Rands
               
                
                for tv in range(size_page_frame):
                    
                    if _pgs_[tv] is not val_Rands:
                        
                        f_variable = False
                        
                        for e in range(xx, val1):
                            if arrList[e] is _pgs_[tv]:
                                f_variable = True
                                if e > numm1:
									
                                    numm1, numm2 = e, tv

                                break
                        
                        if not f_variable:
                            
                            numm2 = tv
                            break


                isFault, n_avail_s= True, numm2
            
            faulty_pages, _pgs_[n_avail_s] = faulty_pages+ 1, arrList[xx]
            
            
            print "\n%d -->>" % (arrList[xx]),
            for zoo in range(size_page_frame):
                if _pgs_[zoo] is not val_Rands:
                    print _pgs_[zoo],
                else:
                    print "[*]", # [*] to be filled
               
        else:
            print "\n%d ->no fault" % (arrList[xx]),
    v_opt=faulty_pages       
    print "\n\nOptimal page replacement had : %d page faults." % (faulty_pages)
    
    
#----------------------------------------------------MAIN METHOD------------------------------------------------------------------------------------------------------------
def main():
	

	val1=int(sys.argv[1])  # get number of pages from the user
	
	
	string1=[]
	
	for i in range(val1):
		string1.append(random.randint(0,9))


	arrayList = string1
	print("Pages: {:<20}\n".format(str(arrayList)))
	
	
	
	
	
	while True:
		print("\nEnter size of page frame between 1 and 7:")
		sizeOfPageFrame = input()
		
		if(sizeOfPageFrame<1 or sizeOfPageFrame>7):
			print("You have inserted wrong input try again.")
			sys.exit(0)
		
			
		print "\n ******************************MENU******************************"
		print("")
		print " 1. First In First Out."
		print " 2. Least Recently Used."
		print " 3. Optimal."
		print " 4. Show all (FIFO, LRU, Optimal)"
		print " 5. Exit program."
		
		choose_option = input("\n Select An option: ")
		
		
		
		
		if choose_option is 1:
		
			first_in_first_out_(sizeOfPageFrame,arrayList,val1)
		
		elif choose_option is 2:
		
			least_recently_used(sizeOfPageFrame,arrayList,val1)
		
		elif choose_option is 3:
		
			optimal_page_replacement(sizeOfPageFrame,arrayList,val1)
		
		elif choose_option is 4:
		    
			first_in_first_out_(sizeOfPageFrame,arrayList,val1)
			least_recently_used(sizeOfPageFrame,arrayList,val1)
			optimal_page_replacement(3,arrayList,val1)
		
		elif choose_option is 5:
			break
	    

if __name__ == "__main__":
	if len(sys.argv) !=2:
		print("Usage: python paging.py [number of pages]")
	else:
		main()  
    
 

   




        




