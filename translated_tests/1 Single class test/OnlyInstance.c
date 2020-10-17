#include"OnlyInstance.h"

// instance fields of the class
struct OnlyInstance {
	 int fieldInitializedAutomatically;
	 int fieldInitializedBeforeConstructor;
	 int privateField;
	 int protectedField;
	 int standardField;
	 int publicField;
	 int counter;
};

// static fields of the class

OnlyInstance new_OnlyInstance(int privateField, int protectedField, int standardField, int publicField){
		OnlyInstance this;
		this.fieldInitializedAutomatically = privateField;
		this.fieldInitializedBeforeConstructor = protectedField;
		this.privateField = privateField;
		this.protectedField = protectedField;
		this.standardField = standardField;
		this.publicField = publicField;
		this.counter = 0;
		return this;
	}

void setCounter(OnlyInstance this, int counter){
		this.counter = counter;
	}

void resetCounter(OnlyInstance this){
		setCounter(this, 0);
	}

int getFieldInitializedAutomatically(OnlyInstance this){
		return this.fieldInitializedAutomatically;
	}

int getFieldInitializedBeforeConstructor(OnlyInstance this){
		return this.fieldInitializedBeforeConstructor;
	}

int getPrivateField(OnlyInstance this){
		return this.privateField;
	}

int getProtectedField(OnlyInstance this){
		return this.protectedField;
	}

int getStandardField(OnlyInstance this){
		return this.standardField;
	}

int getPublicField(OnlyInstance this){
		return this.publicField;
	}

void testContextFields(OnlyInstance this){
		printf("%s\n", this.privateField);
		printf("%s\n", this.protectedField);
		printf("%s\n", this.standardField);
		printf("%s\n", this.publicField);
	}

void testNoContextFields(OnlyInstance this){
		printf("%s\n", privateField);
		printf("%s\n", protectedField);
		printf("%s\n", standardField);
		printf("%s\n", publicField);
	}

void testPrivateMethod(OnlyInstance this){
		printf("Private\n");
	}

void testProtectedMethod(OnlyInstance this){
		printf("Protected\n");
	}

void testPublicMethod(OnlyInstance this){
		printf("Standard\n");
	}

void test(){
		printf("Public\n");
	}

