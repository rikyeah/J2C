public class OnlyStatic {

	private static int fieldInitializedAutomatically;
	private static int fieldInitializedBeforeConstructor = 42;
	private static int privateField;
	protected static int protectedField;
	static int standardField;
	public static int publicField;

	private static int counter;

	public static OnlyInstance createOnlyInstance(int privateField, int protectedField, int standardField, int publicField) {
		return new OnlyInstance(privateField, protectedField, standardField, publicField);
	}

	public static void setCounter(int counter) {
		OnlyStatic.counter = counter;
	}

	public static void resetCounter() {
		OnlyStatic.setCounter(0);
	}

	public static int getFieldInitializedAutomatically() {
		return OnlyStatic.fieldInitializedAutomatically;
	}

	public static int getFieldInitializedBeforeConstructor() {
		return OnlyStatic.fieldInitializedBeforeConstructor;
	}

	public static int getPrivateField() {
		return OnlyStatic.privateField;
	}

	public static int getProtectedField() {
		return OnlyStatic.protectedField;
	}

	public static int getStandardField() {
		return OnlyStatic.standardField;
	}

	public static int getPublicField() {
		return OnlyStatic.publicField;
	}

	public static void testContextFields() {
		System.out.printf("%s\n", OnlyStatic.privateField);
		System.out.printf("%s\n", OnlyStatic.protectedField);
		System.out.printf("%s\n", OnlyStatic.standardField);
		System.out.printf("%s\n", OnlyStatic.publicField);
	}

	public static void testNoContextFields() {
		System.out.printf("%s\n", privateField);
		System.out.printf("%s\n", protectedField);
		System.out.printf("%s\n", standardField);
		System.out.printf("%s\n", publicField);
	}

	private static void testPrivateMethod() {
		System.out.printf("Private\n");
	}

	protected static void testProtectedMethod() {
		System.out.printf("Protected\n");
	}

	static void testStandardMethod() {
		System.out.printf("Standard\n");
	}

	public static void testPublicMethod() {
		System.out.printf("Public\n");
	}

	public static void test() {
		// 0 0 0 0
		System.out.printf("%s\n", OnlyStatic.getPrivateField());
		System.out.printf("%s\n", OnlyStatic.getProtectedField());
		System.out.printf("%s\n", OnlyStatic.getStandardField());
		System.out.printf("%s\n", OnlyStatic.getPublicField());
		// 0 0 0 0
		System.out.printf("%s\n", OnlyStatic.privateField);
		System.out.printf("%s\n", OnlyStatic.protectedField);
		System.out.printf("%s\n", OnlyStatic.standardField);
		System.out.printf("%s\n", OnlyStatic.publicField);

		// 0 0 0 0
		OnlyStatic.testContextFields();
		// 0 0 0 0
		OnlyStatic.testNoContextFields();

		// Private Protected Standard Public
		OnlyStatic.testPrivateMethod();
		OnlyStatic.testProtectedMethod();
		OnlyStatic.testStandardMethod();
		OnlyStatic.testPublicMethod();
	}

}
