import java.util.List;
import java.util.Random;

public class Main {

    public static void main(String[] args) {

        Player player = new Player(15);
        Island island = new Island();
        Random random = new Random();

        while (player.getGunpowder() > 0) {
            List<Terrain> terrains = island.getTerrains();
            Terrain terrain = terrains.get(random.nextInt(terrains.size()));

            boolean success = terrain.hunt(player);

            if (!success) {
                break;
            }
        }

        System.out.println("Hunting completed.");
        System.out.println("Total animals hunted: " + player.getHuntedCount());
        System.out.println("Total meat collected: " + player.getMeat());
    }
}
