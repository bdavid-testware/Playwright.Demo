from playwright.sync_api import sync_playwright, TimeoutError, PlaywrightError

def scrape_title():
    with sync_playwright() as p:
        # Böngésző indítása
        browser = p.chromium.launch(headless=False)  # Ha a böngészőt látható módban szeretnéd indítani, állítsd headless=False-ra
        
        # Új lap létrehozása
        page = browser.new_page()
        
        try:
            # Navigálás a weboldalra
            page.goto("https://www.nemzetisport.hu")
            
            # Várakozás amíg betöltődik az oldal
            page.wait_for_load_state("networkidle")
            
            # A cím lekérése
            title = page.title()
            
            # A cím kiírása
            print(f"Az oldal címe: {title}")
        
        # Hiba kezelés
        except TimeoutError as te:
            print(f"Időtúllépési hiba történt: {te}")
        except PlaywrightError as pwe:
            print(f"Playwright hiba történt: {pwe}")
        except Exception as e:
            print(f"Ismeretlen hiba történt: {e}")
        
        finally:
            # Böngésző bezárása
            browser.close()
            
# A szkript csak akkor fusson, ha közvetlenül futtatják, nem importálják modulként
if __name__ == "__main__":
    scrape_title()