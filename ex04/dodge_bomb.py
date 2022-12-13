import pygame as pg;
import sys;

def main():
    clock = pg.time.Clock();
    pg.display.set_caption("逃げろ！こうかとん！！");
    
    scrn_sfc = pg.display.set_mode((1600,900));
    
    pgbg_sfc = pg.image.load("../fig/pg_bg.jpeg");
    pgbg_rct = pgbg_sfc.get_rect();
    
    #Q3
    tori_sfc = pg.image.load("../fig/6.png");
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0);
    tori_rct = tori_sfc.get_rect();
    tori_rct.center = 900, 400;
    scrn_sfc.blit(tori_sfc, tori_rct);
    
    pg.display.update();
    
    #Q2
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct);
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return;
        
        #キー入力の状態が入る辞書
        #Q4
        key_dict = pg.key.get_pressed();
        if key_dict[pg.K_UP]:
            tori_rct.centery -= 1;
        if key_dict[pg.K_DOWN]:
            tori_rct.centery += 1;
        if key_dict[pg.K_LEFT]:
            tori_rct.centerx -= 1;
        if key_dict[pg.K_RIGHT]:
            tori_rct.centerx += 1;
        scrn_sfc.blit(tori_sfc, tori_rct);
        
        pg.display.update();
        clock.tick(1000);

if __name__ == "__main__":
    pg.init()
    main();
    pg.quit;
    sys.exit;