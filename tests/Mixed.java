
public class Mixed {
	
	private int privateInstanceField;
	int instanceField;
	public int publicInstanceField;
	
	private static int privateStaticField;
	static int staticField;
	public static int publicStaticField;
	
	public static void testStatic(int value) {
		Mixed.privateStaticField = 4;
		Mixed.staticField = value;
		Mixed.publicStaticField = 2;
	}
	
	private static void testStatic2(Mixed mx) {
		mx.testInstance(Mixed.staticField);
		mx.privateInstanceField = Mixed.privateStaticField;
		mx.instanceField = Mixed.staticField;
		mx.publicInstanceField = Mixed.publicStaticField;
	}
	
	public void testInstance(int value) {
		this.privateInstanceField = 4;
		this.instanceField = value;
		this.privateInstanceField = 2;
	}
	
	public void testInstance2() {
		Mixed.privateStaticField = 0;
		Mixed.publicStaticField = 0;
		Mixed.staticField = 0;
		Mixed.testStatic2(this);
		this.testInstance(3);
	}
	
	public Mixed returnArg(Mixed self) {
		return self;
	}
	
	public void testMixed() {
		Mixed mx = new Mixed();
		mx.testInstance(42);
		mx = this.returnArg(new Mixed());
		Mixed.testStatic(42);
		Mixed.testStatic2(mx);
		
	}
}
