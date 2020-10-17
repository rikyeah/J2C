#include"Mixed.h"

// instance fields of the class
struct Mixed {
	 int privateInstanceField;
	 int instanceField;
	 int publicInstanceField;
};

// static fields of the class
int static_privateStaticField;
int static_staticField;
int static_publicStaticField;

void testStatic(int value){
		static_privateStaticField = 4;
		static_staticField = value;
		static_publicStaticField = 2;
	}

void testStatic2(Mixed mx){
		testInstance(mx, static_staticField);
		mx.privateInstanceField = static_privateStaticField;
		mx.instanceField = static_staticField;
		mx.publicInstanceField = static_publicStaticField;
	}

void testInstance(Mixed this, int value){
		this.privateInstanceField = 4;
		this.instanceField = value;
		this.privateInstanceField = 2;
	}

void testInstance2(Mixed this){
		static_privateStaticField = 0;
		static_publicStaticField = 0;
		static_staticField = 0;
		testStatic2(this);
		testInstance(this, 3);
	}

Mixed returnArg(Mixed this, Mixed self){
		return self;
	}

void testMixed(Mixed this){
		Mixed mx = new_Mixed();
		testInstance(mx, 42);
		mx = returnArg(this, new_Mixed());
		testStatic(42);
		testStatic2(mx);
		
	}

