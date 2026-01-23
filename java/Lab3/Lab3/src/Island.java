import java.util.ArrayList;
import java.util.List;

public class Island {

    private final List<Terrain> terrains = new ArrayList<>();

    public Island() {
        terrains.add(new Plain());
        terrains.add(new Mountain());
        terrains.add(new Beach());
    }

    public List<Terrain> getTerrains() {
        return terrains;
    }
}
