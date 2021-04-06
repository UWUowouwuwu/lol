import asyncio
from datetime import datetime, timedelta
from typing import Any, Literal
import discord
from discord.utils import get
from redbot.core import Config, checks, commands
from redbot.core.utils.antispam import AntiSpam
from redbot.core.utils.predicates import MessagePredicate
Cog: Any = getattr(commands, "Cog", object)
RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]
# thanks phen
default = {
    "app_check": False,
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": [],
    "answer5": [],
    "position": [],
    "answer6": [],
    "answer7": [],
    "answer8": [],
    "answer9": [],
    "answer10": [],
    "answer11": [],
    "answer12": [],
    "finalcomments": [],
}
guild_defaults = {
    "app_questions": {
        "question1": None,
        "question2": None,
        "question3": None,
        "question4": None,
        "question5": None,
        "question6": None,
        "question7": None,
        "question8": None,
        "question9": None,
        "question10": None,
        "question11": None,
        "question12": None,
        "finalcomments": "Do you have any final comments for the admins?",
    },
    "applicant_id": None,
    "accepter_id": None,
    "channel_id": None,
    "positions_available": ["this position", "that position"],
}


# Originally from https://github.com/elijabesu/SauriCogs
class CustomApps(Cog):
    """Customize Staff apps for your server"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=73837383738,
            force_registration=True,
        )
        self.config.register_member(**default)
        self.config.register_guild(**guild_defaults)
        self.antispam = {}
    async def red_delete_data_for_user(self, *, requester: RequestType, user_id: int):
        await self.config.member_from_ids(user_id).clear()
    @commands.command()
    @commands.guild_only()
    @checks.bot_has_permissions(manage_roles=True, manage_channels=True, manage_webhooks=True)
    async def apply(self, ctx: commands.Context):
        """Apply to be a staff member."""
        role_add = get(ctx.guild.roles, name="Staff Applicant")
        app_data = await self.config.guild(ctx.guild).app_questions.all()
        user_data = self.config.member(ctx.author)
        channel = get(ctx.guild.text_channels, name="staff-applications")
        if ctx.guild not in self.antispam:
            self.antispam[ctx.guild] = {}
        if ctx.author not in self.antispam[ctx.guild]:
            self.antispam[ctx.guild][ctx.author] = AntiSpam([(timedelta(days=1), 5)])
        if self.antispam[ctx.guild][ctx.author].spammy:
            return await ctx.send("Uh oh, you're doing this way too frequently.")
        if role_add is None:
            return await ctx.send("Uh oh. Looks like your Admins haven't added the required role.")
        if channel is None:
            return await ctx.send(
                "Uh oh. Looks like your Admins haven't added the required channel."
            )
        try:
            await ctx.author.send(
                f"Let's start right away! You have maximum of 5 minutes for each question.\n\nReply with the position you are applying for to continue. To cancel at anytime respond with `cancel`"
            )
        except discord.Forbidden:
            return await ctx.send(f"{ctx.author.mention} I can't DM you. Do you have them closed?")
        await ctx.send(f"Okay, {ctx.author.mention}, I've sent you a DM.")
        def check(m):
            return m.author == ctx.author and m.channel == ctx.author.dm_channel
        try:
            position = await self.bot.wait_for("message", timeout=300, check=check)
            if position.content.lower() == "cancel":
                return await ctx.author.send("Application has been canceled.")
            await user_data.position.set(position.content)
        except asyncio.TimeoutError:
            try:
                await ctx.author.send("You took too long. Try again, please.")
            except discord.HTTPException:
                return await ctx.send(f"Thanks for nothing, {ctx.author.mention}")
            return
        check_1 = app_data["question1"]
        if check_1 is not None:
            await ctx.author.send(app_data["question1"])
            try:
                answer1 = await self.bot.wait_for("message", timeout=300, check=check)
                if answer1.content.lower() == "cancel":
                    return await ctx.author.send("Application has been canceled.")
                await user_data.answer1.set(answer1.content)
            except asyncio.TimeoutError:
                try:
                    await ctx.author.send("You took too long. Try again, please.")
                except discord.HTTPException:
                    return await ctx.send(f"Thanks for nothing, {ctx.author.mention}")
                return
        check_2 = app_data["question2"]
        if check_2 is not None:
            await ctx.author.send(app_data["question2"])
            try:
                answer2 = await self.bot.wait_for("message", timeout=300, check=check)
                if answer2.content.lower() == "cancel":
                    return await ctx.author.send("Application has been canceled.")
                await user_data.answer2.set(answer2.content)
            except asyncio.TimeoutError:
                try:
                    await ctx.author.send("You took too long. Try again, please.")
                except discord.HTTPException:
                    return await ctx.send(f"Thanks for nothing, {ctx.author.mention}")
                return
        check_3 = app_data["question3"]
        if check_3 is not None:
            await ctx.author.send(app_data["question3"])
            try:
                answer3 = await self.bot.wait_for("message", timeout=300, check=check)
                if answer3.content.lower() == "cancel":
                    return await ctx.author.send("Application has been canceled.")
                await user_data.answer3.set(answer3.content)
            except asyncio.TimeoutError:
                try:
                    await ctx.author.send("You took too long. Try again, please.")
                except discord.HTTPException:
                    return await ctx.send(f"Thanks for nothing, {ctx.author.mention}")
                return
        check_4 = app_data["question4"]
        if check_4 is not None:
            await ctx.author.send(app_data["question4"])
            try:
                answer4 = await self.bot.wait_for("message", timeout=300, check=check)
                if answer4.content.lower() == "cancel":
                    return await ctx.author.send("Application has been canceled.")
                await user_data.answer4.set(answer4.content)
            except asyncio.TimeoutError:
                try:
                    await ctx.author.send("You took too long. Try again, please.")
                except discord.HTTPException:
                    return await ctx.send(f"Thanks for nothing, {ctx.author.mention}")
                return
       check_5 = app_data["question5"]
        if check_5 is not None:
            await ctx.author.send(app_data["question5"])
            try:
                answer5 = await self.bot.wait_for("message", timeout=300, check=check)
                if answer5.content.lower() == "cancel":
                    return await ctx.author.send("Application has been canceled.")
                await user_data.answer5.set(answer5.content)
            except asyncio.TimeoutError:
                try:
                    await ctx.author.send("You took too long. Try again, please.")
                except discord.HTTPException:
                    return await ctx.send(f"Thanks for nothing, {ctx.author.mention}")
                return
        check_6 = app_data["question6"]
        if check_6 is not None:
            await ctx.author.send(app_data["question6"])
            try:
                answer6 = await self.bot.wait_for("message", timeout=300, check=check)
                if answer6.content.lower() == "cancel":
                    return await ctx.author.send("Application has been canceled.")
                await user_data.answer6.set(answer6.content)
            except asyncio.TimeoutError:
                try:
                    await ctx.author.send("You took too long. Try again, please.")
                except discord.HTTPException:
                    return await ctx.send(f"Thanks for nothing, {ctx.author.mention}")
                return
        check_7 = app_data["question7"]
        if check_7 is not None:
            await ctx.author.send(app_data["question7"])
            try:
                answer7 = await self.bot.wait_for("message", timeout=300, check=check)
                if answer7.content.lower() == "cancel":
                    return await ctx.author.send("Application has been canceled.")
                await user_data.answer7.set(answer7.content)
            except asyncio.TimeoutError:
                try:
                    await ctx.author.send("You took too long. Try again, please.")
                except discord.HTTPException:
                    return await ctx.send(f"Thanks for nothing, {ctx.author.mention}")
                return
        check_8 = app_data["question8"]
        if check_8 is not None:
            await ctx.author.send(app_data["question8"])
            try:
                answer8 = await self.bot.wait_for("message", timeout=300, check=check)
                if answer8.content.lower() == "cancel":
                    return await ctx.author.send("Application has been canceled.")
                await user_data.answer8.set(answer8.content)
            except asyncio.TimeoutError:
                try:
                    await ctx.author.send("You took too long. Try again, please.")
                except discord.HTTPException:
                    return await ctx.send(f"Thanks for nothing, {ctx.author.mention}")
                return
        check_9 = app_data["question9"]
        if check_9 is not None:
            await ctx.author.send(app_data["question9"])
            try:
                answer9 = await self.bot.wait_for("message", timeout=300, check=check)
                if answer9.content.lower() == "cancel":
                    return await ctx.author.send("Application has been canceled.")
                await user_data.answer9.set(answer9.content)
            except asyncio.TimeoutError:
                try:
                    await ctx.author.send("You took too long. Try again, please.")
                except discord.HTTPException:
                    return await ctx.send(f"Thanks for nothing, {ctx.author.mention}")
                return
        check_10 = app_data["question10"]
        if check_10 is not None:
            await ctx.author.send(app_data["question10"])
            try:
                answer10 = await self.bot.wait_for("message", timeout=300, check=check)
                if answer10.content.lower() == "cancel":
                    return await ctx.author.send("Application has been canceled.")
                await user_data.answer10.set(answer10.content)
            except asyncio.TimeoutError:
                try:
                    await ctx.author.send("You took too long. Try again, please.")
                except discord.HTTPException:
                    return await ctx.send(f"Thanks for nothing, {ctx.author.mention}")
                return
        check_11 = app_data["question11"]
        if check_11 is not None:
            await ctx.author.send(app_data["question11"])
            try:
                answer11 = await self.bot.wait_for("message", timeout=300, check=check)
                if answer11.content.lower() == "cancel":
                    return await ctx.author.send("Application has been canceled.")
                await user_data.answer11.set(answer11.content)
            except asyncio.TimeoutError:
                try:
                    await ctx.author.send("You took too long. Try again, please.")
                except discord.HTTPException:
                    return await ctx.send(f"Thanks for nothing, {ctx.author.mention}")
                return
        check_12 = app_data["question12"]
        if check_12 is not None:
            await ctx.author.send(app_data["question12"])
            try:
                answer12 = await self.bot.wait_for("message", timeout=300, check=check)
                if answer12.content.lower() == "cancel":
                    return await ctx.author.send("Application has been canceled.")
                await user_data.answer12.set(answer12.content)
            except asyncio.TimeoutError:
                try:
                    await ctx.author.send("You took too long. Try again, please.")
                except discord.HTTPException:
                    return await ctx.send(f"Thanks for nothing, {ctx.author.mention}")
                return
        await ctx.author.send(app_data["finalcomments"])
        try:
            finalcomments = await self.bot.wait_for("message", timeout=300, check=check)
            if finalcomments.content.lower() == "cancel":
                return await ctx.author.send("Application has been canceled.")
            await user_data.finalcomments.set(finalcomments.content)
        except asyncio.TimeoutError:
            return await ctx.author.send("You took too long. Try again, please.")
       
        embed = discord.Embed(color=await ctx.embed_colour(), timestamp=datetime.utcnow())
        embed.set_author(name="New application!", icon_url=ctx.author.avatar_url)
        embed.set_footer(
            text=f"{ctx.author.name}#{ctx.author.discriminator} UserID: {ctx.author.id})"
        )
        embed.title = f"User: {ctx.author.mention} {ctx.author.name}#{ctx.author.discriminator} | ID: ({ctx.author.id})"
        )
        if check_1 is not None:
            embed.add_field(name=app_data["question8"], value=answer1.content, inline=False)
        if check_2 is not None:
            embed.add_field(name=app_data["question8"], value=answer2.content, inline=False)
        if check_3 is not None:
            embed.add_field(name=app_data["question8"], value=answer3.content, inline=False)
        if check_4 is not None:
            embed.add_field(name=app_data["question8"], value=answer4.content, inline=False)
        if check_5 is not None:
            embed.add_field(name=app_data["question8"], value=answer5.content, inline=False)
        if check_6 is not None:
            embed.add_field(name=app_data["question8"], value=answer6.content, inline=False)
        if check_7 is not None:
            embed.add_field(name=app_data["question8"], value=answer7.content, inline=False)
        if check_8 is not None:
            embed.add_field(name=app_data["question8"], value=answer8.content, inline=False)
        if check_9 is not None:
            embed.add_field(name=app_data["question9"], value=answer9.content, inline=False)
        if check_10 is not None:
            embed.add_field(name=app_data["question10"], value=answer10.content, inline=False)
        if check_11 is not None:
            embed.add_field(
                name=app_data["question11"],
                value=answer11.content,
                inline=False,
            )
        if check_12 is not None:
            embed.add_field(
                name=app_data["question12"],
                value=answer12.content,
                inline=False,
            )
        embed.add_field(name="Final Comments", value=finalcomments.content, inline=False)
        try:
            webhook = None
            for hook in await channel.webhooks():
                if hook.name == ctx.guild.me.name:
                    webhook = hook
            if webhook is None:
                webhook = await channel.create_webhook(name=ctx.guild.me.name)
            await webhook.send(
                embed=embed, username=ctx.guild.me.display_name, avatar_url=ctx.guild.me.avatar_url
            )
        except discord.HTTPException:
            return await ctx.author.send(
                "Your final application was too long to resolve as an embed. Give this another shot, keeping answers a bit shorter."
            )
        except commands.CommandInvokeError:
            return await ctx.author.send(
                "You need to start over but this time when it asks for year of birth, respond only with a 4 digit year i.e `1999`"
            )
        await ctx.author.add_roles(role_add)
        try:
            await ctx.author.send(
                f"Your application has been sent to {ctx.guild.name} Admins! Thanks for your interest!"
            )
        except commands.CommandInvokeError:
            return await ctx.send(
                f"{ctx.author.mention} I sent your app to the admins. Thanks for closing dms early tho rude ass"
            )
        self.antispam[ctx.guild][ctx.author].stamp()
        await self.config.member(ctx.author).app_check.set(True)
    @checks.admin_or_permissions(manage_guild=True)
    @commands.group(name="appq", aliases=["appquestions"])
    @commands.guild_only()
    async def app_questions(self, ctx: commands.Context):
        """Set/see the custom questions for the applications in your server"""
        app_questions = await self.config.guild(ctx.guild).app_questions.get_raw()
        question_1 = app_questions["question1"]
        question_2 = app_questions["question2"]
        question_3 = app_questions["question3"]
        question_4 = app_questions["question4"]
        question_5 = app_questions["question5"]
        question_6 = app_questions["question6"]
        question_7 = app_questions["question7"]
        question_8 = app_questions["question8"]
        question_9 = app_questions["question9"]
        question_10 = app_questions["question10"]
        question_11 = app_questions["question11"]
        question_12 = app_questions["question12"]
        question_13 = app_questions["finalcomments"]
        await ctx.send(
            "There are 13 questions in this application feature, with a few preloaded already for you.\nHere is the current configuration:"
        )
        e = discord.Embed(colour=await ctx.embed_colour())
        e.add_field(
            name="Question 1", value=f"{question_1}" if question_1 else "Not Set", inline=False
        )
        e.add_field(
            name="Question 2", value=f"{question_2}" if question_2 else "Not Set", inline=False
        )
        e.add_field(
            name="Question 3", value=f"{question_3}" if question_3 else "Not Set", inline=False
        )
        e.add_field(
            name="Question 4", value=f"{question_4}" if question_4 else "Not Set", inline=False
        )
        e.add_field(
            name="Question 5", value=f"{question_5}" if question_5 else "Not Set", inline=False
        )
        e.add_field(
            name="Question 6", value=f"{question_6}" if question_6 else "Not Set", inline=False
        )
        e.add_field(
            name="Question 7", value=f"{question_7}" if question_7 else "Not Set", inline=False
        )
        e.add_field(
            name="Question 8", value=f"{question_8}" if question_8 else "Not Set", inline=False
        )
        e.add_field(
            name="Question 9", value=f"{question_9}" if question_9 else "Not Set", inline=False
        )
        e.add_field(
            name="Question 10", value=f"{question_10}" if question_10 else "Not Set", inline=False
        )
        e.add_field(
            name="Question 11", value=f"{question_11}" if question_11 else "Not Set", inline=False
        )
        e.add_field(
            name="Question 12", value=f"{question_12}" if question_12 else "Not Set", inline=False
        )
        e.add_field(
            name="Question 13", value=f"{question_13}" if question_13 else "Not Set", inline=False
        )
        await ctx.send(embed=e)
    @app_questions.command(name="set")
    async def set_questions(self, ctx: commands.Context):
        """Set up custom questions for your server"""
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        await ctx.send(
            "Let's set up those questions we've not pre-filled:\nYou will be setting questions 8-12. You can view the preloaded questions by passing `{}appq`. To begin, reply with `admin abuse` *spelled exact*".format(
                ctx.prefix
            )
        )
        try:
            confirmation = await ctx.bot.wait_for("message", check=check, timeout=20)
            if confirmation.content.lower() != "admin abuse":
                return await ctx.send("Alright, let's do these later then")
        except asyncio.TimeoutError:
            return await ctx.send(
                "Took to long to respond, gotta be smarter than the users you're hiring for sure."
            )
        app_questions = await self.config.guild(ctx.guild).app_questions.get_raw()
        question_1 = app_questions["question1"]
        question_2 = app_questions["question2"]
        question_3 = app_questions["question3"]
        question_4 = app_questions["question4"]
        question_5 = app_questions["question5"]
        question_6 = app_questions["question6"]
        question_7 = app_questions["question7"]
        question_8 = app_questions["question8"]
        question_9 = app_questions["question9"]
        question_10 = app_questions["question10"]
        question_11 = app_questions["question11"]
        question_12 = app_questions["question12"]
        await ctx.send(
            "Alright, let's start with question 1: You have 5min to decide and respond with question you'd like, or respond with cancel to do this later"
        )
        if question_1 is not None:
            await ctx.send(
                f"Looks like question 1 is currently `{question_1}`:\n Do you want to change this? Type `no` to skip or the question you wish to change to if you want to change."
            )
            try:
                submit_1 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_1.content.lower() != "no":
                    if len(submit_1.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question1.set(
                        submit_1.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
        if question_1 is None:
            try:
                submit_1 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_1.content.lower() != "cancel":
                    if len(submit_1.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question1.set(
                        submit_1.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
            await ctx.send("Moving to question 2: Please respond with your next app question")
        if question_3 is not None:
            await ctx.send(
                f"Looks like question 2 is currently `{question_2}`:\n Do you want to change this? Type `no` to skip or the question you wish to change to if you want to change."
            )
            try:
                submit_2 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_2.content.lower() != "no":
                    if len(submit_2.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question2.set(
                        submit_2.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
        if question_2 is None:
            try:
                submit_2 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_2.content.lower() != "cancel":
                    if len(submit_2.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question2.set(
                        submit_2.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
            await ctx.send("Moving to question 3: Please respond with your next app question")
        if question_3 is not None:
            await ctx.send(
                f"Looks like question 3 is currently `{question_3}`:\n Do you want to change this? Type `no` to skip or the question you wish to change to if you want to change."
            )
            try:
                submit_3 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_3.content.lower() != "no":
                    if len(submit_3.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question3.set(
                        submit_3.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
        if question_3 is None:
            try:
                submit_3 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_3.content.lower() != "cancel":
                    if len(submit_3.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question3.set(
                        submit_3.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
            await ctx.send("Moving to question 4: Please respond with your next app question")
        if question_4 is not None:
            await ctx.send(
                f"Looks like question 4 is currently `{question_4}`:\n Do you want to change this? Type `no` to skip or the question you wish to change to if you want to change."
            )
            try:
                submit_4 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_4.content.lower() != "no":
                    if len(submit_4.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question4.set(
                        submit_4.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
        if question_4 is None:
            try:
                submit_4 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_4.content.lower() != "cancel":
                    if len(submit_4.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question4.set(
                        submit_4.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
            await ctx.send("Moving to question 5: Please respond with your next app question") 
        if question_5 is not None:
            await ctx.send(
                f"Looks like question 5 is currently `{question_5}`:\n Do you want to change this? Type `no` to skip or the question you wish to change to if you want to change."
            )
            try:
                submit_5 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_5.content.lower() != "no":
                    if len(submit_5.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question5.set(
                        submit_5.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
        if question_5 is None:
            try:
                submit_5 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_5.content.lower() != "cancel":
                    if len(submit_5.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question5.set(
                        submit_5.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
            await ctx.send("Moving to question 6: Please respond with your next app question") 
        if question_6 is not None:
            await ctx.send(
                f"Looks like question 6 is currently `{question_6}`:\n Do you want to change this? Type `no` to skip or the question you wish to change to if you want to change."
            )
            try:
                submit_6 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_6.content.lower() != "no":
                    if len(submit_6.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question6.set(
                        submit_6.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
        if question_6 is None:
            try:
                submit_6 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_6.content.lower() != "cancel":
                    if len(submit_6.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question6.set(
                        submit_6.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
            await ctx.send("Moving to question 7: Please respond with your next app question") 
        if question_7 is not None:
            await ctx.send(
                f"Looks like question 7 is currently `{question_7}`:\n Do you want to change this? Type `no` to skip or the question you wish to change to if you want to change."
            )
            try:
                submit_7 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_7.content.lower() != "no":
                    if len(submit_7.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question7.set(
                        submit_7.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
        if question_7 is None:
            try:
                submit_7 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_7.content.lower() != "cancel":
                    if len(submit_7.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question7.set(
                        submit_7.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
            await ctx.send("Moving to question 8: Please respond with your next app question") 
        if question_8 is not None:
            await ctx.send(
                f"Looks like question 8 is currently `{question_8}`:\n Do you want to change this? Type `no` to skip or the question you wish to change to if you want to change."
            )
            try:
                submit_8 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_8.content.lower() != "no":
                    if len(submit_8.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question8.set(
                        submit_8.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
        if question_8 is None:
            try:
                submit_8 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_8.content.lower() != "cancel":
                    if len(submit_8.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question8.set(
                        submit_8.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
            await ctx.send("Moving to question 9: Please respond with your next app question")
        if question_9 is not None:
            await ctx.send(
                f"Looks like question 9 is currently `{question_9}`:\n Do you want to change this? Type `no` to skip or the question you wish to change to if you want to change."
            )
            try:
                submit_9 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_9.content.lower() != "no":
                    if len(submit_9.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question9.set(
                        submit_9.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
            await ctx.send("Moving to question 10: Please respond with your next app question")
        if question_9 is None:
            try:
                submit_9 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_9.content.lower() != "cancel":
                    if len(submit_9.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question9.set(
                        submit_9.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
            await ctx.send("Moving to question 10: Please respond with your next app question")
        if question_10 is not None:
            await ctx.send(
                f"Looks like question 10 is currently `{question_10}`:\n Do you want to change this? Type `no` to skip or the question you wish to change to if you want to change."
            )
            try:
                submit_10 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_10.content.lower() != "no":
                    if len(submit_10.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question10.set(
                        submit_10.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
            await ctx.send("Moving to question 11: Please respond with your next app question")
        if question_10 is None:
            try:
                submit_10 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_10.content.lower() != "cancel":
                    if len(submit_10.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question10.set(
                        submit_10.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
            await ctx.send("Moving to question 11: Please respond with your next app question")
        if question_11 is not None:
            await ctx.send(
                f"Looks like question 11 is currently `{question_11}`:\n Do you want to change this? Type `no` to skip or the question you wish to change to if you want to change."
            )
            try:
                submit_11 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_11.content.lower() != "no":
                    if len(submit_11.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question11.set(
                        submit_11.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
            await ctx.send("Moving to question 12: Please respond with your next app question")
        if question_11 is None:
            try:
                submit_11 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_11.content.lower() != "cancel":
                    if len(submit_11.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question11.set(
                        submit_11.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
            await ctx.send("Moving to question 12: Please respond with your next app question")
        if question_12 is not None:
            await ctx.send(
                f"Looks like question 12 is currently `{question_12}`:\n Do you want to change this? Type `no` to skip or the question you wish to change to if you want to change."
            )
            try:
                submit_12 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_12.content.lower() != "no":
                    if len(submit_12.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question12.set(
                        submit_12.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
        if question_12 is None:
            try:
                submit_12 = await ctx.bot.wait_for("message", check=check, timeout=300)
                if submit_12.content.lower() != "cancel":
                    if len(submit_12.content) > 750:
                        return await ctx.send(
                            "Talkitive are we? Too many characters to fit in final embed, shorten the question some"
                        )
                    await self.config.guild(ctx.guild).app_questions.question12.set(
                        submit_12.content
                    )
            except asyncio.TimeoutError:
                return await ctx.send(
                    "Took too long bud. Let's be coherent for this and try again."
                )
        await ctx.send(
            "That's all the questions and your apps are set *maybe, if you answered, anyway*. Check this with `{}appq`".format(
                ctx.prefix
            )
        )
        
    @checks.admin_or_permissions(administrator=True)
    @commands.command()
    @commands.guild_only()
    @checks.bot_has_permissions(manage_channels=True, manage_roles=True)
    async def applysetup(self, ctx: commands.Context):
        """Go through the initial setup process."""
        pred = MessagePredicate.yes_or_no(ctx)
        role = MessagePredicate.valid_role(ctx)
        applicant = get(ctx.guild.roles, name="Staff Applicant")
        channel = get(ctx.guild.text_channels, name="staff-applications")
        await ctx.send(
            "This will create required channel and role. Do you wish to continue? (yes/no)"
        )
        try:
            await self.bot.wait_for("message", timeout=30, check=pred)
        except asyncio.TimeoutError:
            return await ctx.send("You took too long. Try again, please.")
        if not pred.result:
            return await ctx.send("Setup cancelled.")
        if not applicant:
            try:
                applicant = await ctx.guild.create_role(
                    name="Staff Applicant", reason="Application cog setup"
                )
            except discord.Forbidden:
                return await ctx.send(
                    "Uh oh. Looks like I don't have permissions to manage roles."
                )
        if not channel:
            await ctx.send("Do you want everyone to see the applications channel? (yes/no)")
            try:
                await self.bot.wait_for("message", timeout=30, check=pred)
            except asyncio.TimeoutError:
                return await ctx.send("You took too long. Try again, please.")
            if pred.result:
                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False),
                    ctx.guild.me: discord.PermissionOverwrite(send_messages=True),
                }
            else:
                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
                }
            try:
                channel = await ctx.guild.create_text_channel(
                    "staff-applications",
                    overwrites=overwrites,
                    reason="Application cog setup",
                )
            except discord.Forbidden:
                return await ctx.send(
                    "Uh oh. Looks like I don't have permissions to manage channels."
                )
        await ctx.send(f"What role can accept or reject applicants?")
        try:
            await self.bot.wait_for("message", timeout=30, check=role)
        except asyncio.TimeoutError:
            return await ctx.send("You took too long. Try again, please.")
        accepter = role.result
        await self.config.guild(ctx.guild).applicant_id.set(applicant.id)
        await self.config.guild(ctx.guild).channel_id.set(channel.id)
        await self.config.guild(ctx.guild).accepter_id.set(accepter.id)
        await ctx.send(
            "You have finished the setup! Please, move your new channel to the category you want it in."
        )
    @commands.command()
    @commands.guild_only()
    @checks.bot_has_permissions(manage_roles=True)
    async def accept(self, ctx: commands.Context, target: discord.Member):
        """Accept a staff applicant.
        <target> can be a mention or an ID."""
        try:
            accepter = get(ctx.guild.roles, id=await self.config.guild(ctx.guild).accepter_id())
        except TypeError:
            accepter = None
        if not accepter:
            if not ctx.author.guild_permissions.administrator:
                return await ctx.send("Uh oh, you cannot use this command.")
        else:
            if accepter not in ctx.author.roles:
                return await ctx.send("Uh oh, you cannot use this command.")
        try:
            applicant = get(ctx.guild.roles, id=await self.config.guild(ctx.guild).applicant_id())
        except TypeError:
            applicant = None
        if not applicant:
            applicant = get(ctx.guild.roles, name="Staff Applicant")
            if not applicant:
                return await ctx.send(
                    "Uh oh, the configuration is not correct. Ask the Admins to set it."
                )
        role = MessagePredicate.valid_role(ctx)
        if applicant in target.roles:
            await ctx.send(f"What role do you want to accept {target.name} as?")
            try:
                await self.bot.wait_for("message", timeout=30, check=role)
            except asyncio.TimeoutError:
                return await ctx.send("You took too long. Try again, please.")
            role_add = role.result
            try:
                await target.add_roles(role_add)
            except discord.Forbidden:
                return await ctx.send(
                    "Uh oh, I cannot give them the role. It might be above all of my roles."
                )
            await target.remove_roles(applicant)
            await ctx.send(f"Accepted {target.mention} as {role_add}.")
            await target.send(f"You have been accepted as {role_add} in {ctx.guild.name}.")
        else:
            await ctx.send(f"Uh oh. Looks like {target.mention} hasn't applied for anything.")
    @commands.command()
    @commands.guild_only()
    @checks.bot_has_permissions(manage_roles=True)
    async def deny(self, ctx: commands.Context, target: discord.Member):
        """Deny a staff applicant.
        <target> can be a mention or an ID"""
        try:
            accepter = get(ctx.guild.roles, id=await self.config.guild(ctx.guild).accepter_id())
        except TypeError:
            accepter = None
        if not accepter:
            if not ctx.author.guild_permissions.administrator:
                return await ctx.send("Uh oh, you cannot use this command.")
        else:
            if accepter not in ctx.author.roles:
                return await ctx.send("Uh oh, you cannot use this command.")
        try:
            applicant = get(ctx.guild.roles, id=await self.config.guild(ctx.guild).applicant_id())
        except TypeError:
            applicant = None
        if not applicant:
            applicant = get(ctx.guild.roles, name="Staff Applicant")
            if not applicant:
                return await ctx.send(
                    "Uh oh, the configuration is not correct. Ask the Admins to set it."
                )
        if applicant in target.roles:
            await ctx.send("Would you like to specify a reason? (yes/no)")
            pred = MessagePredicate.yes_or_no(ctx)
            try:
                await self.bot.wait_for("message", timeout=30, check=pred)
            except asyncio.TimeoutError:
                return await ctx.send("You took too long. Try again, please.")
            if pred.result:
                await ctx.send("Please, specify your reason now.")
                def check(m):
                    return m.author == ctx.author
                try:
                    reason = await self.bot.wait_for("message", timeout=120, check=check)
                except asyncio.TimeoutError:
                    return await ctx.send("You took too long. Try again, please.")
                await target.send(
                    f"Your application in {ctx.guild.name} has been denied.\n*Reason:* {reason.content}"
                )
            else:
                await target.send(f"Your application in {ctx.guild.name} has been denied.")
            await target.remove_roles(applicant)
            await ctx.send(f"Denied {target.mention}'s application.")
        else:
            await ctx.send(f"Uh oh. Looks like {target.mention} hasn't applied for anything.")
    @app_questions.command(name="reset")
    async def clear_config(self, ctx: commands.Context):
        """
        Fully resets server configuation to default, and clears all custom app questions
        """
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        await ctx.send(
            "Are you certain about this? This will wipe all settings/custom questions in your server's configuration\nType: `RESET THIS GUILD` to continue (must be typed exact)"
        )
        try:
            confirm_reset = await ctx.bot.wait_for("message", check=check, timeout=30)
            if confirm_reset.content != "RESET THIS GUILD":
                return await ctx.send("Okay, not resetting today")
        except asyncio.TimeoutError:
            return await ctx.send("You took too long to reply")
        await self.config.guild(ctx.guild).app_questions.clear_raw()
        await ctx.send("Guild Reset, goodluck")
