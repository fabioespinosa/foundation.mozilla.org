# Generated by Django 2.2.13 on 2020-07-08 22:15

from django.db import migrations, models
import networkapi.wagtailpages.pagemodels.blog.blog_category
import wagtail.core.blocks
import wagtail.core.blocks.static_block
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('mozfest', '0001_to_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='mozfesthomepage',
            name='banner_guide_text_fy_NL',
            field=models.CharField(blank=True, help_text='A banner paragraph specific to the homepage', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='mozfesthomepage',
            name='banner_heading_fy_NL',
            field=models.CharField(blank=True, help_text='A banner heading specific to the homepage', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='mozfesthomepage',
            name='banner_video_url_fy_NL',
            field=models.URLField(blank=True, help_text='The video to play when users click "watch video"', max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='mozfesthomepage',
            name='cta_button_label_fy_NL',
            field=models.CharField(blank=True, help_text='Label text for the CTA button in the primary nav bar', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='mozfestprimarypage',
            name='body_fy_NL',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'large', 'h2', 'h3', 'h4', 'h5', 'ol', 'ul', 'link', 'hr'])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL that this caption should link out to.', required=False))])), ('image_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'link'])), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this image should link out to.', required=False)), ('top_divider', wagtail.core.blocks.BooleanBlock(help_text='Optional divider above content block.', required=False)), ('bottom_divider', wagtail.core.blocks.BooleanBlock(help_text='Optional divider below content block.', required=False))])), ('image_text_mini', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('altText', wagtail.core.blocks.CharBlock(help_text='Image description (for screen readers).', required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link']))])), ('image_grid', wagtail.core.blocks.StructBlock([('grid_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(help_text='Please remember to properly attribute any images we use.', required=False)), ('url', wagtail.core.blocks.CharBlock(help_text='Optional URL that this figure should link out to.', required=False)), ('square_image', wagtail.core.blocks.BooleanBlock(default=True, help_text='If left checked, the image will be cropped to be square.', required=False))])))])), ('video', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.CharBlock(help_text='To make sure a video will embed properly, go to your YouTube video and click “Share,” then “Embed,” and then copy and paste the provided URL only. For example: https://www.youtube.com/embed/3FIVXBawyQw')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL for caption to link to.', required=False))])), ('iframe', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.CharBlock(help_text='Please note that only URLs from white-listed domains will work.')), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('captionURL', wagtail.core.blocks.CharBlock(help_text='Optional URL that this caption should link out to.', required=False))])), ('linkbutton', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock()), ('URL', wagtail.core.blocks.CharBlock()), ('styling', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary button'), ('btn-secondary', 'Secondary button')]))])), ('spacer', wagtail.core.blocks.StructBlock([('size', wagtail.core.blocks.ChoiceBlock(choices=[('1', 'quarter spacing'), ('2', 'half spacing'), ('3', 'single spacing'), ('4', 'one and a half spacing'), ('5', 'triple spacing')]))])), ('quote', wagtail.core.blocks.StructBlock([('quotes', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.CharBlock()), ('attribution', wagtail.core.blocks.CharBlock())])))])), ('pulse_listing', wagtail.core.blocks.StructBlock([('search_terms', wagtail.core.blocks.CharBlock(help_text='Test your search at mozillapulse.org/search', label='Search', required=False)), ('max_number_of_results', wagtail.core.blocks.IntegerBlock(default=6, help_text='Choose 1-12. If you want visitors to see more, link to a search or tag on Pulse.', max_value=12, min_value=0, required=True)), ('only_featured_entries', wagtail.core.blocks.BooleanBlock(default=False, help_text='Featured items are selected by Pulse moderators.', label='Display only featured entries', required=False)), ('newest_first', wagtail.core.blocks.ChoiceBlock(choices=[('True', 'Show newer entries first'), ('False', 'Show older entries first')], label='Sort')), ('advanced_filter_header', wagtail.core.blocks.static_block.StaticBlock(admin_text='-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------', label=' ')), ('issues', wagtail.core.blocks.ChoiceBlock(choices=[('all', 'All'), ('Decentralization', 'Decentralization'), ('Digital Inclusion', 'Digital Inclusion'), ('Online Privacy & Security', 'Online Privacy & Security'), ('Open Innovation', 'Open Innovation'), ('Web Literacy', 'Web Literacy')])), ('help', wagtail.core.blocks.ChoiceBlock(choices=[('all', 'All'), ('Attend', 'Attend'), ('Create content', 'Create content'), ('Code', 'Code'), ('Design', 'Design'), ('Fundraise', 'Fundraise'), ('Join community', 'Join community'), ('Localize & translate', 'Localize & translate'), ('Mentor', 'Mentor'), ('Plan & organize', 'Plan & organize'), ('Promote', 'Promote'), ('Take action', 'Take action'), ('Test & feedback', 'Test & feedback'), ('Write documentation', 'Write documentation')], label='Type of help needed')), ('direct_link', wagtail.core.blocks.BooleanBlock(default=False, help_text='Checked: user goes to project link. Unchecked: user goes to pulse entry', label='Direct link', required=False))])), ('profile_listing', wagtail.core.blocks.StructBlock([('max_number_of_results', wagtail.core.blocks.IntegerBlock(default=12, help_text='Pick up to 48 profiles.', max_value=48, min_value=1, required=True)), ('advanced_filter_header', wagtail.core.blocks.static_block.StaticBlock(admin_text='-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------', label=' ')), ('profile_type', wagtail.core.blocks.CharBlock(default='', help_text='Example: Fellow.', required=False)), ('program_type', wagtail.core.blocks.CharBlock(default='', help_text='Example: Tech Policy.', required=False)), ('year', wagtail.core.blocks.CharBlock(default='', required=False))])), ('profile_by_id', wagtail.core.blocks.StructBlock([('ids', wagtail.core.blocks.CharBlock(help_text='Show profiles for pulse users with specific profile ids (mozillapulse.org/profile/[##]). For multiple profiles, specify a comma separated list (e.g. 85,105,332).', label='Profile by ID'))])), ('profile_directory', wagtail.core.blocks.StructBlock([('max_number_of_results', wagtail.core.blocks.IntegerBlock(default=12, help_text='Pick up to 48 profiles.', max_value=48, min_value=1, required=True)), ('advanced_filter_header', wagtail.core.blocks.static_block.StaticBlock(admin_text='-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------', label=' ')), ('profile_type', wagtail.core.blocks.CharBlock(default='', help_text='Example: Fellow.', required=False)), ('program_type', wagtail.core.blocks.CharBlock(default='', help_text='Example: Tech Policy.', required=False)), ('year', wagtail.core.blocks.CharBlock(default='', required=False)), ('filter_values', wagtail.core.blocks.CharBlock(default='2019,2018,2017,2016,2015,2014,2013', help_text='Example: 2019,2018,2017,2016,2015,2014,2013', required=True))])), ('recent_blog_entries', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('tag_filter', wagtail.core.blocks.CharBlock(help_text='Test this filter at foundation.mozilla.org/blog/tags/', label='Filter by Tag', required=False)), ('category_filter', wagtail.core.blocks.ChoiceBlock(choices=networkapi.wagtailpages.pagemodels.blog.blog_category.BlogPageCategory.get_categories, help_text='Test this filter at foundation.mozilla.org/blog/category/', label='Filter by Category', required=False)), ('top_divider', wagtail.core.blocks.BooleanBlock(help_text='Optional divider above content block.', required=False)), ('bottom_divider', wagtail.core.blocks.BooleanBlock(help_text='Optional divider below content block.', required=False))])), ('airtable', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(help_text="Copied from the Airtable embed code. The word 'embed' will be in the url")), ('height', wagtail.core.blocks.IntegerBlock(default=533, help_text='The height of the view on a desktop, usually copied from the Airtable embed code'))])), ('typeform', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(help_text='The URL of the published Typeform')), ('button_type', wagtail.core.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary button'), ('btn-secondary', 'Secondary button')])), ('button_text', wagtail.core.blocks.CharBlock(required=True))]))], null=True),
        ),
        migrations.AddField(
            model_name='mozfestprimarypage',
            name='header_fy_NL',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='mozfestprimarypage',
            name='intro_fy_NL',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Page intro content', null=True),
        ),
    ]
