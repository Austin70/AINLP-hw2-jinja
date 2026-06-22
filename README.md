Project Overview  
This project demonstrates how Jinja templating can be used to generate dynamic prompts for rewriting recipe instructions. The task involves taking a raw recipe and generating clearer, more accessible versions for different skill levels.

Why Jinja?  
Jinja is appropriate for this task because:
Conditional Logic: Different instructions for beginner vs advanced cooks
Loops: Process variable-length ingredient lists and steps
Reusable Components: Common patterns like "heat pan" or "mix ingredients"
Optional Sections: Safety notes that don't always appear
Multiple Prompt Variants: Different output formats from same structure

Template Features  
The Jinja template prompt_template.j2 uses:
Conditional rendering based on skill level
Loops through ingredients and steps
Optional sections for safety notes
Multiple prompt variants for different audiences


Key Advantages of Jinja Over Simple String Formatting  
Conditional Sections: Template handles different difficulty levels appropriately
Loops: Ingredients and steps are processed systematically
Reusable Components: Common patterns defined once and reused
Optional Sections: Safety notes that appear only when needed
Multiple Variants: Easy to generate different output formats
