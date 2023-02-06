### **[Pacmann]Python Project**
# **Cashier Self Service System**
Repository for Self Service Cashier Project
## **A. Introduction**
This project is the final assignment of Pacmann’s python course. With this project, I am expected to be able to solve the given case by implementing python learning as a solution

###### **Project Background**
This project was motivated by the needs of Andi, who is a supermarket owner. Andi aims to create a cashier self-service digital system. Thus, customers can carry out the transaction process independently, and can also be accessed by customers outside the city.
Andi request us to provide the system (programming using Python) with some features on this system.

###### **Project Objective**
- Provide cashier self-service system with Python with the requested features
- Ensure the system has fulfilled all of Andi’s requests and needs
- Do a test on the system that has been created and make sure it runs well

## **B. Feature & Requirements**
Based on Andi’s need there is some mandatory feature on our system there are:
- add_item ⇒ to add the item name, quantity, and the price
- update_item_name ⇒ to change the item name if the first input is the wrong value
- update_item_qty ⇒ to change the quantity if the first input is the wrong value
- update_item_price ⇒ to change the price if the first input is the wrong value
- delete_item ⇒ to remove one of the items that have been inputted
- reset_transaction ⇒ to remove all items
- check_order ⇒ to check the item has been inputted in the table form
- total_price ⇒ to calculate the total price before discount
- total_cost (additional) ⇒ to calculate the total cost after discount

This feature should be arranged on 2 documents py those are:
- transaction.py (document modular code contains: class and function)
- cashier.py (document cashier self-service system code)

Library:
- Pandas

## **C. Flowchart**
For the cashier self-service system, We need a flowchart to know the expected logic flow that can be translated into python code.
Below is a flowchart for the cashier system that we developed:
![This is an image](https://github.com/thoriqcholidy/Pacmann-Self-Service-Cashier/blob/master/flowchart.png)

## **D. Function and Attributes**
Please find the function and attributes below:

![This is an image](https://github.com/thoriqcholidy/Pacmann-Self-Service-Cashier/blob/master/function.png)

> 💡Note:
>
> Discount rule:
> - if total price > Rp 200000 ⇒ discount = 5%
> - if total price > Rp 300000 ⇒ discount = 8%
> - if total price > Rp 500000 ⇒ discount = 10%

## **E. Test Case**
##### **Test 1 (Add item)** 
Customer added item, there are:
- Ayam Goreng ⇒ Quantity: 2, Price: 20000
- Pasta Gigi  ⇒ Quantity: 3, Price: 15000

Result:

![This is an image](https://github.com/thoriqcholidy/Pacmann-Self-Service-Cashier/blob/master/test1.png)

##### **Test 2 (Remove one item)**
Customer removed "Pasta Gigi"

Result:

![This is an image](https://github.com/thoriqcholidy/Pacmann-Self-Service-Cashier/blob/master/test2.png)

##### **Test 3 (Remove all item)**
Customer removed all item

Result:

![This is an image](https://github.com/thoriqcholidy/Pacmann-Self-Service-Cashier/blob/master/test3.png)

##### **Test 4 (Check and total order)**
Customer finish the shopping and then want to knows the total price and total cost of their item.
The item are:
- Ayam Goreng  ⇒ Quantity: 2, Price: 20000
- Pasta Gigi   ⇒ Quantity: 3, Price: 15000
- Mainan Mobil ⇒ Quantity: 1, Price: 200000
- Mi Instan    ⇒ Quantity: 5, Price: 3000

Check the item first before share the total price/cost

Result:
- Check Order:

![This is an image](https://github.com/thoriqcholidy/Pacmann-Self-Service-Cashier/blob/master/test4.png)

- Total Price & Cost

![This is an image](https://github.com/thoriqcholidy/Pacmann-Self-Service-Cashier/blob/master/test4_total.png)

##### **Test 5 (Additional test case update item)**
Customer made some changes on the items:
- Item name ⇒ "Ayam Goreng" to "Ayam goreng"
- Quantity  ⇒ 2 to 3
- Item name ⇒ 20000 to 19000

Result:

![This is an image](https://github.com/thoriqcholidy/Pacmann-Self-Service-Cashier/blob/master/test5.png)

##### **Test 6 (Additional test case ValueError)**
The system already prevents users to input the wrong data type for the process. 
Below is the test case if the user input the wrong data type

![This is an image](https://github.com/thoriqcholidy/Pacmann-Self-Service-Cashier/blob/master/test6.png)

##### **Test 7 (Additional test case KeyError)**
The system already prevents user to input the worng "key" for the process.
Below is the test case if the user input the wrong "key"

![This is an image](https://github.com/thoriqcholidy/Pacmann-Self-Service-Cashier/blob/master/test7.png)


## **F. Conclusion**
With the result of the test for the python script (code) that have created, it can be concluded that:
1. The script on [cashier.py](https://github.com/thoriqcholidy/Pacmann-Self-Service-Cashier/blob/master/chasier.py) can be used to satisfy Andi's needs with the requirements that have been requested, which features have been defined in the modular [transaction.py](https://github.com/thoriqcholidy/Pacmann-Self-Service-Cashier/blob/master/transaction.py)
2. The features and requirements Andi's need already covered on the system has been developed
3. Currently, the system is running well and also has efective responses when an error occurs (user input wrong data/type)


## **G. Closing**
Thank you for your attention to review and check this project. 
I am willing to accept any feedback and suggestions that can help me become better in the future. 
Kindly contact to my email: 📫thoriqcholidy@gmail.com


**Author** Copyright(c) *2023 M Thoriq Cholidy*







