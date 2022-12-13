import pygame as pg;
import random;
import sys;
import time;
yoko, tate = 1, 1;
def check_bound(obj_rct, scr_rct):
    yoko, tate = 1, 1;
    #第1引数はこうかとんや爆弾rct
    #第2引数は画面のrect
    #範囲内+1/範囲外-1
    if obj_rct.left < scr_rct.left-100 or obj_rct.right > scr_rct.right+100:
        yoko = -1;
    if obj_rct.top < scr_rct.top-100 or obj_rct.bottom > scr_rct.bottom+100:
        tate = -1;
    return yoko, tate;
    
def main():
    global yoko, tate;
    count_item = 0;
    game_time = pg.time.get_ticks();
    clock = pg.time.Clock();
    pg.display.set_caption("逃げろ！こうかとん！！");
    
    scrn_sfc = pg.display.set_mode((1600,900));
    scrn_rct = scrn_sfc.get_rect();
    
    
    pgbg_sfc = pg.image.load("../fig/pg_bg.jpeg");
    pgbg_rct = pgbg_sfc.get_rect();
    
    #クリア表示、アイテム数表示
    #fonto = pg.font.Font(None, 80);
    #txt = fonto.render(count_item, True,(0,0,255));
    #scrn_sfc.blit(txt, (0, 0));
    
    #Q3
    tori_sfc = pg.image.load("../fig/6.png");
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0);
    tori_rct = tori_sfc.get_rect();
    tori_rct.center = 900, 400;
    scrn_sfc.blit(tori_sfc, tori_rct);
    
    pg.display.update();
    
    #Q5 爆弾作成
    bomb_sfc = pg.image.load("../fig/bomb.png");
    bomb_sfc = pg.transform.rotozoom(bomb_sfc, 0, 0.3);
    bomb_rct = bomb_sfc.get_rect();
    bomb_rct.centerx = random.randint(10, scrn_rct.width);
    bomb_rct.centery = random.randint(10, scrn_rct.height);
    scrn_sfc.blit(bomb_sfc, bomb_rct);
    
    #added 追加アイテム　八王子ラーメン
    item_sfc = pg.image.load("../fig/8_ramen.jpeg");
    item_sfc = pg.transform.rotozoom(item_sfc, 0, 0.3);
    item_rct = item_sfc.get_rect();
    item_rct.centerx = random.randint(10, scrn_rct.width);
    item_rct.centery = random.randint(10, scrn_rct.height);
    scrn_sfc.blit(item_sfc, item_rct);
    
    #added 仲間かまとぅ
    kama_sfc = pg.image.load("../fig/かまとぅ.png");
    kama_sfc = pg.transform.rotozoom(kama_sfc, 0, 0.8);
    kama_rct = kama_sfc.get_rect();
    kama_rct.center = 700, 400;
    scrn_sfc.blit(kama_sfc, kama_rct);
    
    pg.display.update();
    
    
    #爆弾とラーメンの移動方向
    vx, vy = +1, +1;
    ix, iy = +1, +1;
    #Q2
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct);
        #scrn_sfc.blit(txt, (0, 0));
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return;
        
        #Q4 こうかとん移動
        key_dict = pg.key.get_pressed();
        if key_dict[pg.K_UP]:
            tori_rct.centery -= 1;
        if key_dict[pg.K_DOWN]:
            tori_rct.centery += 1;
        if key_dict[pg.K_LEFT]:
            tori_rct.centerx -= 1;
        if key_dict[pg.K_RIGHT]:
            tori_rct.centerx += 1;
            
        #かまとぅ 移動
        if key_dict[pg.K_w]:
            kama_rct.centery -= 1;
        if key_dict[pg.K_x]:
            kama_rct.centery += 1;
        if key_dict[pg.K_a]:
            kama_rct.centerx -= 1;
        if key_dict[pg.K_d]:
            kama_rct.centerx += 1;
            
        #こうかとん 壁判定    
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
        scrn_sfc.blit(kama_sfc, kama_rct);
        scrn_sfc.blit(item_sfc, item_rct);
        
        #障害物系の反射
        bomb_rct.move_ip(vx, vy);
        item_rct.move_ip(vx, vy);
        yoko, tate = check_bound(bomb_rct, scrn_rct);
        itemx, itemy = check_bound(item_rct, scrn_rct);
        vx *= yoko;
        vy *= tate;
        ix *= itemx;
        iy *= itemy;
        scrn_sfc.blit(bomb_sfc, bomb_rct);
        
        if tori_rct.colliderect(bomb_rct) or kama_rct.colliderect(bomb_rct):
            return;
        if tori_rct.colliderect(item_rct) or kama_rct.colliderect(item_rct):
            count_item += 1;
        
        if count_item == 10:
            break;
        #game_time = time.time - start;
        pg.display.update();
        clock.tick(1000);
        

if __name__ == "__main__":
    pg.init()
    main();
    pg.quit;
    sys.exit;