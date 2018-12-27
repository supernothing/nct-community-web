# Generated by Django 2.1.4 on 2018-12-26 17:16

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('avatar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('activity_type', models.CharField(blank=True, choices=[('new_bounty', 'New Bounty'), ('start_work', 'Work Started'), ('stop_work', 'Work Stopped'), ('work_submitted', 'Work Submitted'), ('work_done', 'Work Done'), ('worker_approved', 'Worker Approved'), ('worker_rejected', 'Worker Rejected'), ('worker_applied', 'Worker Applied'), ('increased_bounty', 'Increased Funding'), ('killed_bounty', 'Canceled Bounty'), ('new_tip', 'New Tip'), ('receive_tip', 'Tip Received'), ('bounty_abandonment_escalation_to_mods', 'Escalated for Abandonment of Bounty'), ('bounty_abandonment_warning', 'Warning for Abandonment of Bounty'), ('bounty_removed_slashed_by_staff', 'Dinged and Removed from Bounty by Staff'), ('bounty_removed_by_staff', 'Removed from Bounty by Staff'), ('bounty_removed_by_funder', 'Removed from Bounty by Funder'), ('new_crowdfund', 'New Crowdfund Contribution'), ('new_grant', 'New Grant'), ('update_grant', 'Updated Grant'), ('killed_grant', 'Cancelled Grant'), ('new_grant_contribution', 'Contributed to Grant'), ('killed_grant_contribution', 'Cancelled Grant Contribution'), ('new_milestone', 'New Milestone'), ('update_milestone', 'Updated Milestone'), ('new_kudos', 'New Kudos')], db_index=True, max_length=50)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('needs_review', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BlockedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('handle', models.CharField(db_index=True, max_length=255, unique=True)),
                ('comments', models.TextField(blank=True, default='')),
                ('active', models.BooleanField(help_text='Is the block active?')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bounty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('web3_type', models.CharField(default='bounties_network', max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('web3_created', models.DateTimeField(db_index=True)),
                ('value_in_token', models.DecimalField(decimal_places=2, default=1, max_digits=50)),
                ('token_name', models.CharField(max_length=50)),
                ('token_address', models.CharField(max_length=50)),
                ('bounty_type', models.CharField(blank=True, choices=[('Bug', 'Bug'), ('Security', 'Security'), ('Feature', 'Feature'), ('Unknown', 'Unknown')], max_length=50)),
                ('project_length', models.CharField(blank=True, choices=[('Hours', 'Hours'), ('Days', 'Days'), ('Weeks', 'Weeks'), ('Months', 'Months'), ('Unknown', 'Unknown')], max_length=50)),
                ('experience_level', models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Unknown', 'Unknown')], max_length=50)),
                ('github_url', models.URLField(db_index=True)),
                ('github_issue_details', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('github_comments', models.IntegerField(default=0)),
                ('bounty_owner_address', models.CharField(max_length=50)),
                ('bounty_owner_email', models.CharField(blank=True, max_length=255)),
                ('bounty_owner_github_username', models.CharField(blank=True, max_length=255)),
                ('bounty_owner_name', models.CharField(blank=True, max_length=255)),
                ('is_open', models.BooleanField(help_text='Whether the bounty is still open for fulfillments.')),
                ('expires_date', models.DateTimeField()),
                ('raw_data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('current_bounty', models.BooleanField(default=False, help_text='Whether this bounty is the most current revision one or not')),
                ('_val_usd_db', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('contract_address', models.CharField(default='', max_length=50)),
                ('network', models.CharField(blank=True, db_index=True, max_length=255)),
                ('idx_experience_level', models.IntegerField(db_index=True, default=0)),
                ('idx_project_length', models.IntegerField(db_index=True, default=0)),
                ('idx_status', models.CharField(choices=[('cancelled', 'cancelled'), ('done', 'done'), ('expired', 'expired'), ('open', 'open'), ('started', 'started'), ('submitted', 'submitted'), ('unknown', 'unknown')], db_index=True, default='open', max_length=9)),
                ('issue_description', models.TextField(blank=True, default='')),
                ('funding_organisation', models.CharField(blank=True, default='', max_length=255)),
                ('standard_bounties_id', models.IntegerField(default=0)),
                ('num_fulfillments', models.IntegerField(default=0)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('accepted', models.BooleanField(default=False, help_text='Whether the bounty has been done')),
                ('interested_comment', models.IntegerField(blank=True, null=True)),
                ('submissions_comment', models.IntegerField(blank=True, null=True)),
                ('override_status', models.CharField(blank=True, max_length=255)),
                ('last_comment_date', models.DateTimeField(blank=True, null=True)),
                ('fulfillment_accepted_on', models.DateTimeField(blank=True, null=True)),
                ('fulfillment_submitted_on', models.DateTimeField(blank=True, null=True)),
                ('fulfillment_started_on', models.DateTimeField(blank=True, null=True)),
                ('canceled_on', models.DateTimeField(blank=True, null=True)),
                ('canceled_bounty_reason', models.TextField(blank=True, default='', verbose_name='Cancelation reason')),
                ('project_type', models.CharField(choices=[('traditional', 'traditional'), ('contest', 'contest'), ('cooperative', 'cooperative')], default='traditional', max_length=50)),
                ('permission_type', models.CharField(choices=[('permissionless', 'permissionless'), ('approval', 'approval')], default='permissionless', max_length=50)),
                ('snooze_warnings_for_days', models.IntegerField(default=0)),
                ('token_value_time_peg', models.DateTimeField(blank=True, null=True)),
                ('token_value_in_usdt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True)),
                ('value_in_usdt_now', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True)),
                ('value_in_usdt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True)),
                ('value_in_eth', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True)),
                ('value_true', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True)),
                ('privacy_preferences', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('admin_override_and_hide', models.BooleanField(default=False, help_text='Admin override to hide the bounty from the system')),
                ('admin_override_suspend_auto_approval', models.BooleanField(default=False, help_text='Admin override to suspend work auto approvals')),
                ('admin_mark_as_remarket_ready', models.BooleanField(default=False, help_text='Admin override to mark as remarketing ready')),
                ('attached_job_description', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Bounties',
            },
        ),
        migrations.CreateModel(
            name='BountyFulfillment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('fulfiller_address', models.CharField(max_length=50)),
                ('fulfiller_email', models.CharField(blank=True, max_length=255)),
                ('fulfiller_github_username', models.CharField(blank=True, max_length=255)),
                ('fulfiller_name', models.CharField(blank=True, max_length=255)),
                ('fulfiller_metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('fulfillment_id', models.IntegerField(blank=True, null=True)),
                ('fulfiller_hours_worked', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True)),
                ('fulfiller_github_url', models.CharField(blank=True, max_length=255, null=True)),
                ('accepted', models.BooleanField(default=False)),
                ('accepted_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BountySyncRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('github_url', models.URLField()),
                ('processed', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CoinRedemption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('shortcode', models.CharField(default='', max_length=255)),
                ('url', models.URLField(null=True)),
                ('network', models.CharField(default='', max_length=255)),
                ('token_name', models.CharField(max_length=255)),
                ('contract_address', models.CharField(max_length=255)),
                ('amount', models.IntegerField(default=1)),
                ('expires_date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Coin Redemptions',
            },
        ),
        migrations.CreateModel(
            name='CoinRedemptionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('ip', models.GenericIPAddressField(protocol='IPv4')),
                ('txid', models.CharField(default='', max_length=255)),
                ('txaddress', models.CharField(max_length=255)),
                ('sent_on', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Coin Redemption Requests',
            },
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date Created')),
                ('issue_message', models.TextField(blank=True, default='', verbose_name='Issue Comment')),
                ('pending', models.BooleanField(default=False, help_text='If this option is chosen, this interest is pending and not yet active', verbose_name='Pending')),
                ('acceptance_date', models.DateTimeField(blank=True, null=True, verbose_name='Date Accepted')),
                ('status', models.CharField(choices=[('review', 'Needs Review'), ('warned', 'Hunter Warned'), ('okay', 'Okay'), ('snoozed', 'Snoozed'), ('pending', 'Pending')], default='okay', help_text='Whether or not the interest requires review', max_length=7, verbose_name='Needs Review')),
            ],
        ),
        migrations.CreateModel(
            name='LabsResearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('link', models.URLField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='labs')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('handle', models.CharField(db_index=True, max_length=255, unique=True)),
                ('last_sync_date', models.DateTimeField(null=True)),
                ('email', models.CharField(blank=True, db_index=True, max_length=255)),
                ('github_access_token', models.CharField(blank=True, db_index=True, max_length=255)),
                ('pref_lang_code', models.CharField(blank=True, choices=[('en', 'English'), ('es', 'Spanish'), ('de', 'German'), ('hi', 'Hindi'), ('it', 'Italian'), ('ko', 'Korean'), ('pl', 'Polish'), ('ja', 'Japanese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese')], max_length=2)),
                ('slack_repos', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, size=None)),
                ('slack_token', models.CharField(blank=True, default='', max_length=255)),
                ('slack_channel', models.CharField(blank=True, default='', max_length=255)),
                ('discord_repos', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, size=None)),
                ('discord_webhook_url', models.CharField(blank=True, default='', max_length=400)),
                ('suppress_leaderboard', models.BooleanField(default=False, help_text='If this option is chosen, we will remove your profile information from the leaderboard')),
                ('hide_profile', models.BooleanField(default=True, help_text='If this option is chosen, we will remove your profile information all_together')),
                ('trust_profile', models.BooleanField(default=False, help_text='If this option is chosen, the user is able to submit a faucet/ens domain registration even if they are new to github')),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, size=None)),
                ('organizations', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, size=None)),
                ('form_submission_records', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list)),
                ('max_num_issues_start_work', models.IntegerField(default=3)),
                ('preferred_payout_address', models.CharField(blank=True, default='', max_length=255)),
                ('max_tip_amount_usdt_per_tx', models.DecimalField(decimal_places=2, default=500, max_digits=50)),
                ('max_tip_amount_usdt_per_week', models.DecimalField(decimal_places=2, default=1500, max_digits=50)),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='avatar.Avatar')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Search History',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('email', models.EmailField(max_length=255)),
                ('raw_data', models.TextField()),
                ('ip', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('web3_type', models.CharField(default='v3', max_length=50)),
                ('emails', django.contrib.postgres.fields.jsonb.JSONField(blank=True)),
                ('url', models.CharField(blank=True, default='', max_length=255)),
                ('primary_email', models.CharField(blank=True, default='', max_length=255)),
                ('tokenName', models.CharField(default='ETH', max_length=255)),
                ('tokenAddress', models.CharField(blank=True, max_length=255)),
                ('amount', models.DecimalField(decimal_places=4, default=1, max_digits=50)),
                ('comments_public', models.TextField(blank=True, default='')),
                ('ip', models.CharField(max_length=50)),
                ('github_url', models.URLField(blank=True, null=True)),
                ('from_name', models.CharField(blank=True, default='', max_length=255)),
                ('from_email', models.CharField(blank=True, default='', max_length=255)),
                ('from_username', models.CharField(blank=True, default='', max_length=255)),
                ('username', models.CharField(blank=True, default='', max_length=255)),
                ('network', models.CharField(default='', max_length=255)),
                ('txid', models.CharField(default='', max_length=255)),
                ('receive_txid', models.CharField(blank=True, default='', max_length=255)),
                ('received_on', models.DateTimeField(blank=True, null=True)),
                ('from_address', models.CharField(blank=True, default='', max_length=255)),
                ('receive_address', models.CharField(blank=True, default='', max_length=255)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('is_for_bounty_fulfiller', models.BooleanField(default=False, help_text='If this option is chosen, this tip will be automatically paid to the bounty fulfiller, not self.usernameusername.')),
                ('tx_status', models.CharField(choices=[('na', 'na'), ('pending', 'pending'), ('success', 'success'), ('error', 'error'), ('unknown', 'unknown'), ('dropped', 'dropped')], db_index=True, default='na', max_length=9)),
                ('receive_tx_status', models.CharField(choices=[('na', 'na'), ('pending', 'pending'), ('success', 'success'), ('error', 'error'), ('unknown', 'unknown'), ('dropped', 'dropped')], db_index=True, default='na', max_length=9)),
                ('tx_time', models.DateTimeField(blank=True, null=True)),
                ('receive_tx_time', models.DateTimeField(blank=True, null=True)),
                ('expires_date', models.DateTimeField(blank=True, null=True)),
                ('comments_priv', models.TextField(blank=True, default='')),
                ('recipient_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_tips', to='dashboard.Profile')),
                ('sender_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_tips', to='dashboard.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TokenApproval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('coinbase', models.CharField(max_length=50)),
                ('token_name', models.CharField(max_length=50)),
                ('token_address', models.CharField(max_length=50)),
                ('approved_address', models.CharField(max_length=50)),
                ('approved_name', models.CharField(max_length=50)),
                ('tx', models.CharField(default='', max_length=255)),
                ('network', models.CharField(default='', max_length=255)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='token_approvals', to='dashboard.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('AD', 'advanced'), ('TO', 'gas'), ('AL', 'alpha'), ('BA', 'basic'), ('BU', 'tools to build'), ('CS', 'coming soon'), ('CO', 'community'), ('FF', 'just for fun')], max_length=2)),
                ('img', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('url_name', models.CharField(blank=True, max_length=40)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('link_copy', models.CharField(blank=True, max_length=255)),
                ('active', models.BooleanField(default=False)),
                ('new', models.BooleanField(default=False)),
                ('stat_graph', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ToolVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='dashboard.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='UserAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('action', models.CharField(choices=[('Login', 'Login'), ('Logout', 'Logout'), ('added_slack_integration', 'Added Slack Integration'), ('removed_slack_integration', 'Removed Slack Integration'), ('updated_avatar', 'Updated Avatar'), ('account_disconnected', 'Account Disconnected')], max_length=50)),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('location_data', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('utm', django.contrib.postgres.fields.jsonb.JSONField(default=dict, null=True)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='dashboard.Profile')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='tool',
            name='votes',
            field=models.ManyToManyField(blank=True, to='dashboard.ToolVote'),
        ),
    ]
