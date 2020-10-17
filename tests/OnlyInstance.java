public class OnlyInstance {

	private int fieldInitializedAutomatically;
	private int fieldInitializedBeforeConstructor = 42;
	private int privateField;
	protected int protectedField;
	int standardField;
	public int publicField;

	private int counter;

	public OnlyInstance(int privateField, int protectedField, int standardField, int publicField) {
		this.fieldInitializedAutomatically = privateField;
		this.fieldInitializedBeforeConstructor = protectedField;
		this.privateField = privateField;
		this.protectedField = protectedField;
		this.standardField = standardField;
		this.publicField = publicField;
		this.counter = 0;
	}

	public void setCounter(int counter) {
		this.counter = counter;
	}

	public void resetCounter() {
		this.setCounter(0);
	}

	public int getFieldInitializedAutomatically() {
		return this.fieldInitializedAutomatically;
	}

	public int getFieldInitializedBeforeConstructor() {
		return this.fieldInitializedBeforeConstructor;
	}

	public int getPrivateField() {
		return this.privateField;
	}

	public int getProtectedField() {
		return this.protectedField;
	}

	public int getStandardField() {
		return this.standardField;
	}

	public int getPublicField() {
		return this.publicField;
	}

	public void testContextFields() {
		System.out.printf("%s\n", this.privateField);
		System.out.printf("%s\n", this.protectedField);
		System.out.printf("%s\n", this.standardField);
		System.out.printf("%s\n", this.publicField);
	}

	public void testNoContextFields() {
		System.out.printf("%s\n", privateField);
		System.out.printf("%s\n", protectedField);
		System.out.printf("%s\n", standardField);
		System.out.printf("%s\n", publicField);
	}

	private void testPrivateMethod() {
		System.out.printf("Private\n");
	}

	protected void testProtectedMethod() {
		System.out.printf("Protected\n");
	}

	void testStandardMethod() {
		System.out.printf("Standard\n");
	}

	public void testPublicMethod() {
		System.out.printf("Public\n");
	}

	public static void test() {
		OnlyInstance oi = new OnlyInstance(1, 2, 3, 4);

		// 1 2 3 4
		System.out.printf("%s\n", oi.getPrivateField());
		System.out.printf("%s\n", oi.getProtectedField());
		System.out.printf("%s\n", oi.getStandardField());
		System.out.printf("%s\n", oi.getPublicField());
		// 1 2 3 4
		System.out.printf("%s\n", oi.privateField);
		System.out.printf("%s\n", oi.protectedField);
		System.out.printf("%s\n", oi.standardField);
		System.out.printf("%s\n", oi.publicField);

		// 1 2 3 4
		oi.testContextFields();
		// 1 2 3 4
		oi.testNoContextFields();

		// Private Protected Standard Public
		oi.testPrivateMethod();
		oi.testProtectedMethod();
		oi.testStandardMethod();
		oi.testPublicMethod();
	}

}
