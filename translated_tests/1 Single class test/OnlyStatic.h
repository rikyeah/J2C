#ifndef ONLYSTATIC_H
#define ONLYSTATIC_H


typedef struct OnlyStatic OnlyStatic;

OnlyInstance createOnlyInstance(int privateField, int protectedField, int standardField, int publicField);
void setCounter(int counter);
void resetCounter();
int getFieldInitializedAutomatically();
int getFieldInitializedBeforeConstructor();
int getPrivateField();
int getProtectedField();
int getStandardField();
int getPublicField();
void testContextFields();
void testNoContextFields();
void testPublicMethod();
void test();

#endif