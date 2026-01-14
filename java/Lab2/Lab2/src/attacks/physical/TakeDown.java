package attacks.physical;

import ru.ifmo.se.pokemon.*;

public class TakeDown extends PhysicalMove {
    public TakeDown() {
        super(Type.NORMAL, 90, 85);
    }

    @Override
    protected void applySelfDamage(Pokemon attacker, double damage){
        double recoil = damage * 0.25;
        recoil = Math.round(recoil);
        if (recoil < 1) recoil = 1;

        attacker.setMod(Stat.HP, (int)recoil);
        System.out.println(attacker + " took recoil damage！");
    }

    @Override
    protected String describe() {
        return "Used Take Down";
    }
}
