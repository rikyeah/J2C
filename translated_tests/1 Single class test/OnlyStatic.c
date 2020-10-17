#include"OnlyStatic.h"

// instance fields of the class
struct OnlyStatic {
};

// static fields of the class
int static_fieldInitializedAutomatically;
int static_fieldInitializedBeforeConstructor;
int static_privateField;
int static_protectedField;
int static_standardField;
int static_publicField;
int static_counter;

OnlyInstance createOnlyInstance(int privateField, int protectedField, int standardField, int publicField){
		return new_OnlyInstance(privateField, protectedField, standardField, publicField);
	}

void setCounter(int counter){
		static_counter = counter;
	}

void resetCounter(){
		setCounter(0);
	}

int getFieldInitializedAutomatically(){
		return static_fieldInitializedAutomatically;
	}

int getFieldInitializedBeforeConstructor(){
		return static_fieldInitializedBeforeConstructor;
	}

int getPrivateField(){
		return static_privateField;
	}

int getProtectedField(){
		return static_protectedField;
	}

int getStandardField(){
		return static_standardField;
	}

int getPublicField(){
		return static_publicField;
	}

void testContextFields(){
		printf("%s\n", static_privateField);
		printf("%s\n", static_protectedField);
		printf("%s\n", static_standardField);
		printf("%s\n", static_publicField);
	}

void testNoContextFields(){
		printf("%s\n", privateField);
		printf("%s\n", protectedField);
		printf("%s\n", standardField);
		printf("%s\n", publicField);
	}

void testPrivateMethod(){
		printf("Private\n");
	}

void testProtectedMethod(){
		printf("Protected\n");
	}

void testStandardMethod(OnlyStatic this){
		printf("Standard\n");
	}

void testPublicMethod(){
		printf("Public\n");
	}

void test(){
		// 0 0 0 0
		printf("%s\n", getPrivateField());
		printf("%s\n", getProtectedField());
		printf("%s\n", getStandardField());
		printf("%s\n", getPublicField());
		// 0 0 0 0
		printf("%s\n", static_privateField);
		printf("%s\n", static_protectedField);
		printf("%s\n", static_standardField);
		printf("%s\n", static_publicField);

		// 0 0 0 0
		testContextFields();
		// 0 0 0 0
		testNoContextFields();

		// Private Protected Standard Public
		testPrivateMethod();
		testProtectedMethod();
		testStandardMethod();
		testPublicMethod();
	}

