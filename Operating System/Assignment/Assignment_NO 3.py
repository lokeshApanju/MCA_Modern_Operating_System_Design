def fifo_page_replacement(pages, frames):
    frame = []
    page_faults = 0
    for page in pages:
        if page not in frame:
            page_faults += 1
            if len(frame) < frames:
                frame.append(page)
            else:
                frame.pop(0)      # Remove oldest page
                frame.append(page)
        print(f"Page: {page} -> Frames: {frame}")
    return page_faults
# Fixed Page Reference String
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3
print("FIFO Page Replacement")
fifo_faults = fifo_page_replacement(pages, frames)
print("Total Page Faults (FIFO):", fifo_faults)

def lru_page_replacement(pages, frames):
    frame = []
    page_faults = 0
    for page in pages:
        if page not in frame:
            page_faults += 1
            if len(frame) < frames:
                frame.append(page)
            else:
                frame.pop(0)      # Remove least recently used page
                frame.append(page)
        else:
            frame.remove(page)
            frame.append(page)    # Move recently used page to end
        print(f"Page: {page} -> Frames: {frame}")
    return page_faults
# Fixed Page Reference String
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frames = 3

print("\nLRU Page Replacement")
lru_faults = lru_page_replacement(pages, frames)
print("Total Page Faults (LRU):", lru_faults)
