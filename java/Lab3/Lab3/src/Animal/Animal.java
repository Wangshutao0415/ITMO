package Animal;

public abstract class Animal {

    private final int meatValue;
    private final int gunpowderCost;
    private final String name;

    protected Animal(String name, int meatValue, int gunpowderCost) {
        this.name = name;
        this.meatValue = meatValue;
        this.gunpowderCost = gunpowderCost;
    }

    public int getMeatValue() {
        return meatValue;
    }

    public int getGunpowderCost() {
        return gunpowderCost;
    }

    public String getName() {
        return name;
    }
}
