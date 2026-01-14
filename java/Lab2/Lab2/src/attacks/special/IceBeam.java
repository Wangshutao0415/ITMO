package attacks.special;

import ru.ifmo.se.pokemon.*;

public class IceBeam  extends SpecialMove {
    public IceBeam() {
        super(Type.ICE, 90, 100.0);

    }

    @Override
    protected void applyOppEffects(Pokemon defender) {

        if (Math.random() <= 0.10) {
            Effect.freeze(defender);
            System.out.println(defender + " Froze！");
        }
    }

    @Override
    protected String describe() {
        return "Used Ice Beam";
    }
}
