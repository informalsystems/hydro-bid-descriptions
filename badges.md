# Badge Definitions Guide

This document explains how to **create new badges** or **update existing badges** inside the repository. It is intended for non-developers and uses clear steps with examples.

---

## Location of Badge Definitions

All badge definitions are stored in the file: **`badge-definitions.json`**.

Each badge is a **JSON object** with the following properties:

```json
"first_time_bidder": {
  "imageUrl": "/images/hex_heart@4x.png",
  "tooltip": "This bid is from a first-time bidder on Hydro. New teams often offer extra tribute or bonuses to win early community trust, and your vote can help them prove their model and unlock future rounds. Consider supporting if you'd like to diversify Hydro's deployments and encourage fresh projects."
}
```

### Explanation of Properties

* **Badge key** (e.g., `"first_time_bidder"`): Unique identifier for the badge. To display this badge, add the key into the **`badges`** array inside `bid-description.json`.
* **`imageUrl`**: Path to the badge image. Images are located inside the **`/images`** folder. To add a new badge image, upload it into this folder and reference it here (e.g., `"/images/new_badge.png"`).
* **`tooltip`**: Text shown when hovering over the badge. The tooltip supports **Markdown formatting**, so you can use **bold**, *italics*, links, lists, etc.

### Dynamic Parameters

Tooltips can include dynamic values using the format: **`${parameter_name}`**.

* Example: `"This bid is paired with ${atomic_bid_title}"`.
* ⚠️ Adding new dynamic parameters requires **developer support**, since code changes are needed to parse them. Currently, this exists for the **`atomic_bid`** badge.

---

## Adding a New Badge

1. **Upload an image** into the `/images` folder (e.g., `new_badge.png`).
2. **Add a new key** in `badge-definitions.json` (e.g., `"new_badge"`).
3. Inside the object, define its properties:

   * `"imageUrl": "/images/new_badge.png"`
   * `"tooltip": "Your tooltip text here (Markdown supported)."`
4. **Commit/Push** your changes to the repository.

---

## Updating an Existing Badge

1. Find the badge in **`badge-definitions.json`**.
2. Modify the **`tooltip`** (you can rewrite or add Markdown).
3. If needed, replace the **`imageUrl`** with a new image.
4. Save and commit your changes.

---

## Adding Badges to a Bid

1. Open **`bid-description.json`**.
2. Find the bid you want to update.
3. Add or update the **`badges`** array. Example:

```json
"badges": ["first_time_bidder", "vortex"]
```

After merging your changes, the bid will show these badges in the UI.

---

## Summary

* **`badge-definitions.json`** → Define badges.
* **`/images`** → Store badge images.
* **`bid-description.json`** → Attach badges to bids.
* **Tooltips support Markdown** → You can style text.
* **Dynamic parameters require developers** → Don’t try to add them alone.

By following these steps, you can easily **add or update badges**.
