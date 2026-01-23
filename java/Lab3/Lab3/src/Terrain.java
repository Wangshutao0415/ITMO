import Animal.Animal;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public abstract class Terrain {

    protected final List<Animal> animals = new ArrayList<>();
    protected final Random random = new Random();

    protected Terrain() {
        spawnAnimals();
    }

    protected abstract void spawnAnimals();

    public List<Animal> getAnimals() {
        return animals;
    }

    public boolean hunt(Player player) {
        Animal best = null;

        for (Animal a : animals) {
            if (player.getGunpowder() >= a.getGunpowderCost()) {
                if (best == null || a.getMeatValue() > best.getMeatValue()) {
                    best = a;
                }
            }
        }

        if (best == null) {
            return false;
        }

        player.consumeGunpowder(best.getGunpowderCost());
        player.addMeat(best.getMeatValue());
        animals.remove(best);

        return true;
    }
}
