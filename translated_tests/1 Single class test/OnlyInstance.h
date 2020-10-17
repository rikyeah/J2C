#ifndef ONLYINSTANCE_H
#define ONLYINSTANCE_H


typedef struct OnlyInstance OnlyInstance;

OnlyInstance new_OnlyInstance(int privateField, int protectedField, int standardField, int publicField);
void setCounter(OnlyInstance this, int counter);
void resetCounter(OnlyInstance this);
int getFieldInitializedAutomatically(OnlyInstance this);
int getFieldInitializedBeforeConstructor(OnlyInstance this);
int getPrivateField(OnlyInstance this);
int getProtectedField(OnlyInstance this);
int getStandardField(OnlyInstance this);
int getPublicField(OnlyInstance this);
void testContextFields(OnlyInstance this);
void testNoContextFields(OnlyInstance this);
void testPublicMethod(OnlyInstance this);
void test();

#endif