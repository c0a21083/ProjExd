import pygame as pg;
import random;
import sys;
yoko, tate = 1, 1;
def check_bound(obj_rct, scr_rct):
    yoko, tate = 1, 1;
    #第1引数はこうかとんや爆弾rect
    #第2引数は画面のrect
    #範囲内+1/範囲外-1
    if obj_rct.left < scr_rct.left or obj_rct.right > scr_rct.right:
        yoko = -1;
    if obj_rct.top < scr_rct.top or obj_rct.bottom > scr_rct.bottom:
        tate = -1;
    return yoko, tate;
def main():
    global yoko, tate;
    clock = pg.time.Clock();
    pg.display.set_caption("逃げろ！こうかとん！！");
    
    scrn_sfc = pg.display.set_mode((1600,900));
    scrn_rct = scrn_sfc.get_rect();
    
    
    pgbg_sfc = pg.image.load("../fig/pg_bg.jpeg");
    pgbg_rct = pgbg_sfc.get_rect();
    
    #Q3
    tori_sfc = pg.image.load("../fig/6.png");
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0);
    tori_rct = tori_sfc.get_rect();
    tori_rct.center = 900, 400;
    scrn_sfc.blit(tori_sfc, tori_rct);
    
    pg.display.update();
    
    #Q5 爆弾作成
    bomb_sfc = pg.Surface((20, 20));
    bomb_sfc.set_colorkey((0, 0, 0));
    pg.draw.circle(bomb_sfc, (255,0,0), (10, 10), 10);
    bomb_rct = bomb_sfc.get_rect();
    bomb_rct.centerx = random.randint(0, scrn_rct.width);
    bomb_rct.centery = random.randint(0, scrn_rct.height);
    scrn_sfc.blit(bomb_sfc, bomb_rct);
    
    
    
    vx, vy = +1, +1;
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
            
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            # どこかしらはみ出ていたら
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1 
                
        scrn_sfc.blit(tori_sfc, tori_rct);
        
        bomb_rct.move_ip(vx, vy);
        yoko, tate = check_bound(bomb_rct, scrn_rct);
        vx *= yoko;
        vy *= tate;
        scrn_sfc.blit(bomb_sfc, bomb_rct);
        
        if tori_rct.colliderect(bomb_rct):
            return;
        
        pg.display.update();
        clock.tick(1000);

if __name__ == "__main__":
    pg.init()
    main();
    pg.quit;
    sys.exit;