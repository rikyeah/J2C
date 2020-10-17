#ifndef MIXED_H
#define MIXED_H


typedef struct Mixed Mixed;

void testStatic(int value);
void testInstance(Mixed this, int value);
void testInstance2(Mixed this);
Mixed returnArg(Mixed this, Mixed self);
void testMixed(Mixed this);

#endif