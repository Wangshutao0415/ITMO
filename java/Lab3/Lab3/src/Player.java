public class Player {

    private int gunpowder;
    private int meat;
    private int huntedCount;

    public Player(int gunpowder) {
        this.gunpowder = gunpowder;
    }

    public int getGunpowder() {
        return gunpowder;
    }

    public int getMeat() {
        return meat;
    }

    public int getHuntedCount() {
        return huntedCount;
    }

    public void consumeGunpowder(int amount) {
        gunpowder -= amount;
    }

    public void addMeat(int amount) {
        meat += amount;
        huntedCount++;
    }
}
