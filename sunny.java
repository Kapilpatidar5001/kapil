class Person {
// complete the class
private String name;
private float age;

public Person()
{
this.name="";
this.age=0;
}

public Person(String name, float age)
{
this.name=name;
this.age=age;
}

public String getName()
{
return this.name;
}

public float getAge()
{
return this.age;
}

public void setName(String name)
{
this.name=name;
}

public void setAge(float age)
{
this.age=age;
}

}


class Account {
// complete the class
public static long accNum;
private double balance;
private Person accHolder;

public Account()
{
this.accNum=0;
this.balance=0;
this.accHolder=null;
}

public Account(String name,float age,double balance)
{
this.accHolder=new Person(name,age);
this.setBalance(balance);
}

public void deposit(double rupees) {
// Set the balance of the account after the money is deposited to the account
this.balance+=rupees;
}

public void withdraw(double rupees) {
// Set the balance of the account after the money is withdrawn from the account
//if(this.balance-rupees>=500)
this.balance-=rupees;
}

public String toString() {
// Should return the string in the format:
// Name: TempName Age: 68.0 AccNumber: 1333339438704 Balance= 899.0
return ("Name: "+this.accHolder.getName()+" "+"Age: "+this.accHolder.getAge()+" "+"AccNumber: "+this.accNum+"\n"+"Balance= "+this.getBalance());
}

public double getBalance() {
// Should return the balance present in the Account
return this.balance;
}

public void setBalance(double bal){
// Set the balance for the account holder
this.balance=bal;
} 

public void setAccountDetails(String name, float age, double balance) {
// Set the account details for the account holder
this.accHolder.setName(name);
this.accHolder.setAge(age);
this.balance=balance;
}

public Person getPerson(){
// return the AccountHolder
return accHolder;
}
}
