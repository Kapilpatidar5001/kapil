class Person {
    // complete the class
    public String name;
    public float age;
   public Person(){
       name="";
       age=0;
   }
    public Person(String name,float age){
        this.name=name;
        this.age=age;
    }
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name=name;
    }
    public float getAge(){
        return age;
    }
    public void setAge(float age){
        this.age=age;
    }
}


class Account {
    public static long accNum=1;
    public static double balance;
    public Person accHolder;
     
     public Account(){
        balance=0;
        accHolder=null;
     }
    public Account(String name,float age,double balance){
        accHolder=this.getPerson();
        this.setAccountDetails(name,age,balance);
        
        
    }
  public void deposit(double rupees) {
    balance=balance+rupees;
  }

  public void withdraw(double rupees) {
   double b=balance;
   if((b-rupees)>500)
   balance=balance-rupees;
   
  }

  public String toString() {
    // Should return the string in the format:
    // Name: TempName Age: 68.0 AccNumber: 1333339438704 Balance= 899.0
    return ("Name: "+accHolder.name+" Age: "+accHolder.age+" AccNumber: "+accNum+" Balance= "+this.balance);
  }

  public double getBalance() {
    // Should return the balance present in the Account
    return balance;
  }
  
  public void setBalance(double bal){
    // Set the balance for the account holder
    balance=bal;
  }  

  public void setAccountDetails(String name, float age, double balance) {
      accHolder.setName(name);
      accHolder.setAge(age);
      this.setBalance(balance);
    // Set the account details for the account holder
    
  }
  
  public Person getPerson(){
    
    Person p=new Person();
    return p;
    // return the AccountHolder
    
  }
}
