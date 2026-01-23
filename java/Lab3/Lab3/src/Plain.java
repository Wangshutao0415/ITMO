import Animal.Bird;
import Animal.Goat;

public class Plain extends Terrain {

    @Override
    protected void spawnAnimals() {
        int birds = random.nextInt(3) + 3;
        int goats = random.nextInt(2) + 2;

        for (int i = 0; i < birds; i++) {
            animals.add(new Bird());
        }
        for (int i = 0; i < goats; i++) {
            animals.add(new Goat());
        }
    }
}
